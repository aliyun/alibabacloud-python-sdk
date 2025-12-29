# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppEventsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        event_type: str = None,
        namespace: str = None,
        object_kind: str = None,
        object_name: str = None,
        page_size: int = None,
        reason: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The page number of the page to return.
        self.current_page = current_page
        # The type of the event. Valid values:
        # 
        # *   **Warning**: an alert.
        # *   **Normal**: a normal event.
        self.event_type = event_type
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The type of the object. Valid values:
        # 
        # *   **Deployment**: an application.
        # *   **Pod**: an application instance.
        # *   **Service**: a Server Load Balancer (SLB) instance.
        # *   **HorizontalPodAutoscaler**: an auto scaling policy.
        # *   **CloneSet**: an application.
        self.object_kind = object_kind
        # The name of the object. Fuzzy search by prefix is supported.
        self.object_name = object_name
        # The number of entries to return on each page. Valid values: 0 to 10000.
        self.page_size = page_size
        # The cause of the event. Fuzzy search by prefix is supported.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

