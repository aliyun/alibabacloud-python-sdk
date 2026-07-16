# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CmsEventForView(DaraModel):
    def __init__(
        self,
        annotations: Dict[str, Any] = None,
        data: Any = None,
        datacontenttype: str = None,
        dataschema: str = None,
        dedup_id: str = None,
        id: str = None,
        integration_uuid: str = None,
        labels: Dict[str, Any] = None,
        receive_time: int = None,
        resource: main_models.EventResourceForEventView = None,
        severity: str = None,
        source: str = None,
        sourcetype: str = None,
        status: str = None,
        subject: str = None,
        subtype: str = None,
        sys_id: str = None,
        time: str = None,
        timestamp: int = None,
        type: str = None,
        workspace: str = None,
        workspace_tags: Dict[str, Any] = None,
    ):
        # Additional annotations for the event. This is an unstructured description field.
        self.annotations = annotations
        # The raw data of the event. The format depends on the event type and dataschema.
        self.data = data
        # The content type of the data field.
        self.datacontenttype = datacontenttype
        # The data schema definition, which describes the structure of the data field.
        self.dataschema = dataschema
        # The deduplication ID. It identifies different instances of the same event, such as a repeatedly reported event.
        self.dedup_id = dedup_id
        # The unique identifier for the event. The system generates this globally unique ID.
        self.id = id
        # The unique integration identifier. It is used for identity recognition in cross-system integrations.
        self.integration_uuid = integration_uuid
        # The key-value pairs of the event labels.
        self.labels = labels
        # The timestamp when the event was received and processed.
        self.receive_time = receive_time
        # Information about the resource associated with the event, such as the instance ID, IP address, and region.
        self.resource = resource
        # The severity level of the event.
        self.severity = severity
        # The name of the source system or service, such as ECS, RDS, or VPC.
        self.source = source
        # The type of event source. It distinguishes between sources such as monitoring systems, Simple Log Service, and application observability.
        self.sourcetype = sourcetype
        # The current status of the event.
        self.status = status
        # The subject or title of the event. It briefly describes the event.
        self.subject = subject
        # The event subtype.
        self.subtype = subtype
        # The internal system event ID. It is used for internal tracking and log association.
        self.sys_id = sys_id
        # The time when the event occurred.
        self.time = time
        # The timestamp of the event occurrence.
        self.timestamp = timestamp
        # The event type.
        self.type = type
        # The ID or name of the workspace. It is used for multi-tenant or organization fencing.
        self.workspace = workspace
        # The workspace tags. They help you manage events by tag.
        self.workspace_tags = workspace_tags

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.data is not None:
            result['data'] = self.data

        if self.datacontenttype is not None:
            result['datacontenttype'] = self.datacontenttype

        if self.dataschema is not None:
            result['dataschema'] = self.dataschema

        if self.dedup_id is not None:
            result['dedupId'] = self.dedup_id

        if self.id is not None:
            result['id'] = self.id

        if self.integration_uuid is not None:
            result['integrationUuid'] = self.integration_uuid

        if self.labels is not None:
            result['labels'] = self.labels

        if self.receive_time is not None:
            result['receiveTime'] = self.receive_time

        if self.resource is not None:
            result['resource'] = self.resource.to_map()

        if self.severity is not None:
            result['severity'] = self.severity

        if self.source is not None:
            result['source'] = self.source

        if self.sourcetype is not None:
            result['sourcetype'] = self.sourcetype

        if self.status is not None:
            result['status'] = self.status

        if self.subject is not None:
            result['subject'] = self.subject

        if self.subtype is not None:
            result['subtype'] = self.subtype

        if self.sys_id is not None:
            result['sysId'] = self.sys_id

        if self.time is not None:
            result['time'] = self.time

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.type is not None:
            result['type'] = self.type

        if self.workspace is not None:
            result['workspace'] = self.workspace

        if self.workspace_tags is not None:
            result['workspaceTags'] = self.workspace_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('datacontenttype') is not None:
            self.datacontenttype = m.get('datacontenttype')

        if m.get('dataschema') is not None:
            self.dataschema = m.get('dataschema')

        if m.get('dedupId') is not None:
            self.dedup_id = m.get('dedupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('integrationUuid') is not None:
            self.integration_uuid = m.get('integrationUuid')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('receiveTime') is not None:
            self.receive_time = m.get('receiveTime')

        if m.get('resource') is not None:
            temp_model = main_models.EventResourceForEventView()
            self.resource = temp_model.from_map(m.get('resource'))

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcetype') is not None:
            self.sourcetype = m.get('sourcetype')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('subtype') is not None:
            self.subtype = m.get('subtype')

        if m.get('sysId') is not None:
            self.sys_id = m.get('sysId')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        if m.get('workspaceTags') is not None:
            self.workspace_tags = m.get('workspaceTags')

        return self

