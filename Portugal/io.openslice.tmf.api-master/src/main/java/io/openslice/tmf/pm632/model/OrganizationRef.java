/*-
 * ========================LICENSE_START=================================
 * io.openslice.tmf.api
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
package io.openslice.tmf.pm632.model;

import java.util.Objects;

import com.fasterxml.jackson.annotation.JsonProperty;

import org.springframework.validation.annotation.Validated;

import io.openslice.tmf.common.model.BaseRootNamedEntity;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.persistence.Entity;
import jakarta.validation.constraints.NotNull;

/**
 * OrganizationRef
 */
@Validated
@jakarta.annotation.Generated(value = "io.swagger.codegen.languages.SpringCodegen", date = "2019-10-19T23:38:47.101+03:00")

@Entity
public class OrganizationRef  extends BaseRootNamedEntity {


  @JsonProperty("@referredType")
  private String referredType = null;


  /**
   * Unique identifier of a related entity.
   * @return id
  **/
  @Schema(description = "Unique identifier of a related entity.")
  @NotNull


  @JsonProperty("id")
  public String getId() {
    return uuid;
  }

  public OrganizationRef referredType(String referredType) {
    this.referredType = referredType;
    return this;
  }

  /**
   * The actual type of the target instance when needed for disambiguation.
   * @return referredType
  **/
  @Schema(description = "The actual type of the target instance when needed for disambiguation.")


  public String getReferredType() {
    return referredType;
  }

  public void setReferredType(String referredType) {
    this.referredType = referredType;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrganizationRef organizationRef = (OrganizationRef) o;
    return Objects.equals(this.uuid, organizationRef.uuid) &&
        Objects.equals(this.href, organizationRef.href) &&
        Objects.equals(this.name, organizationRef.name) &&
        Objects.equals(this.baseType, organizationRef.baseType) &&
        Objects.equals(this.schemaLocation, organizationRef.schemaLocation) &&
        Objects.equals(this.type, organizationRef.type) &&
        Objects.equals(this.referredType, organizationRef.referredType);
  }

  @Override
  public int hashCode() {
    return Objects.hash( uuid, href, name, baseType, schemaLocation, type, referredType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrganizationRef {\n");
    
    sb.append("    id: ").append(toIndentedString(uuid)).append("\n");
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    baseType: ").append(toIndentedString(baseType)).append("\n");
    sb.append("    schemaLocation: ").append(toIndentedString(schemaLocation)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    referredType: ").append(toIndentedString(referredType)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

