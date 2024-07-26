/*-
 * ========================LICENSE_START=================================
 * io.openslice.portal.api
 * %%
 * Copyright (C) 2019 openslice.io
 * %%
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * =========================LICENSE_END==================================
 */


package portal.api.util;

import java.io.UnsupportedEncodingException;
import java.util.Date;
import java.util.Properties;

import javax.mail.Address;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.NoSuchProviderException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

import org.apache.commons.lang3.ArrayUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;

import portal.api.service.PortalPropertiesService;


/**
 * @author ctranoris
 *
 */
@Configuration
public class EmailUtil {


	@Autowired
	static PortalPropertiesService propsService;
	
	private static final transient Log logger = LogFactory.getLog(EmailUtil.class.getName());
	

	@Autowired
	public void setPortalPropertiesService( PortalPropertiesService srv ){
		EmailUtil.propsService = srv;
	}
			
	

	public static void SendRegistrationActivationEmail(String email, String messageBody, String subj) {

		Properties props = new Properties();

		// Session session = Session.getDefaultInstance(props, null);

		props.setProperty("mail.transport.protocol", "smtp");
		props.put("mail.smtp.auth", "true");
		if ((propsService.getPropertyByName("mailhost").getValue() != null)
				&& (!propsService.getPropertyByName("mailhost").getValue().isEmpty()))
			props.setProperty("mail.host", propsService.getPropertyByName("mailhost").getValue());
		if ((propsService.getPropertyByName("mailuser").getValue() != null)
				&& (!propsService.getPropertyByName("mailuser").getValue().isEmpty()))
			props.setProperty("mail.user", propsService.getPropertyByName("mailuser").getValue());
		if ((propsService.getPropertyByName("mailpassword").getValue() != null)
				&& (!propsService.getPropertyByName("mailpassword").getValue().isEmpty()))
			props.setProperty("mail.password", propsService.getPropertyByName("mailpassword").getValue());

		String adminemail = propsService.getPropertyByName("adminEmail").getValue();
		final String username = propsService.getPropertyByName("mailuser").getValue();
		final String password = propsService.getPropertyByName("mailpassword").getValue();

		logger.info("adminemail = " + adminemail);
		logger.info("subj = " + subj);

		Session mailSession = Session.getInstance(props, new javax.mail.Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication(username, password);
			}
		});

		Transport transport;
		try {
			transport = mailSession.getTransport();

			MimeMessage msg = new MimeMessage(mailSession);
			msg.setSentDate(new Date());
			msg.setFrom(new InternetAddress(adminemail, adminemail));
			msg.setSubject(subj);
			msg.setContent(messageBody, "text/html; charset=ISO-8859-1");
			msg.addRecipient(Message.RecipientType.TO, new InternetAddress(email, email));
			msg.addRecipient(Message.RecipientType.CC, new InternetAddress(adminemail, adminemail));

			transport.connect();

			Address[] recips = (Address[]) ArrayUtils.addAll(msg.getRecipients(Message.RecipientType.TO),
					msg.getRecipients(Message.RecipientType.CC));

			transport.sendMessage(msg, recips);

			transport.close();

		} catch (NoSuchProviderException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (MessagingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
