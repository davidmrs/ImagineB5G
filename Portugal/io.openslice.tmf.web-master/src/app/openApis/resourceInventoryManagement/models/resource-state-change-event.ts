/* tslint:disable */
import { ResourceStateChangeEventPayload } from './resource-state-change-event-payload';

/**
 * The notification data structure
 */
export interface ResourceStateChangeEvent {

  /**
   * The correlation id for this event.
   */
  correlationId?: string;

  /**
   * An explnatory of the event.
   */
  description?: string;

  /**
   * The domain of the event.
   */
  domain?: string;
  event?: ResourceStateChangeEventPayload;

  /**
   * The identifier of the notification.
   */
  eventId?: string;

  /**
   * Time of the event occurrence.
   */
  eventTime?: string;

  /**
   * The type of the notification.
   */
  eventType?: string;

  /**
   * A priority.
   */
  priority?: string;

  /**
   * The time the event occured.
   */
  timeOcurred?: string;

  /**
   * The title of the event.
   */
  title?: string;
}
