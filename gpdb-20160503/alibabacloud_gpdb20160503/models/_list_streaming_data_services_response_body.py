# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListStreamingDataServicesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_items: List[main_models.ListStreamingDataServicesResponseBodyServiceItems] = None,
        total_record_count: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns real-time data service items
        self.service_items = service_items
        # Total record count.
        self.total_record_count = total_record_count

    def validate(self):
        if self.service_items:
            for v1 in self.service_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceItems'] = []
        if self.service_items is not None:
            for k1 in self.service_items:
                result['ServiceItems'].append(k1.to_map() if k1 else None)

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_items = []
        if m.get('ServiceItems') is not None:
            for k1 in m.get('ServiceItems'):
                temp_model = main_models.ListStreamingDataServicesResponseBodyServiceItems()
                self.service_items.append(temp_model.from_map(k1))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListStreamingDataServicesResponseBodyServiceItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        service_description: str = None,
        service_id: str = None,
        service_ip: str = None,
        service_managed: bool = None,
        service_name: str = None,
        service_owner_id: str = None,
        service_port: str = None,
        service_spec: str = None,
        service_type: str = None,
        status: str = None,
    ):
        # Creation time.
        self.create_time = create_time
        # Last modified time
        self.modify_time = modify_time
        # Service description.
        self.service_description = service_description
        # Service ID.
        self.service_id = service_id
        # Service IP.
        self.service_ip = service_ip
        # Whether it is a managed service.
        self.service_managed = service_managed
        # Service name.
        self.service_name = service_name
        # Service owner ID.
        self.service_owner_id = service_owner_id
        # Service port.
        self.service_port = service_port
        # Service specification (in CU).
        self.service_spec = service_spec
        # Service type, with the following value:
        # 
        # - **adbpgss**
        self.service_type = service_type
        # Service status, with the following values:
        # 
        # - Init: Initializing
        # 
        # - Running: In operation
        # 
        # - Exception: Abnormal
        # 
        # - Paused: Suspended
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_owner_id is not None:
            result['ServiceOwnerId'] = self.service_owner_id

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceOwnerId') is not None:
            self.service_owner_id = m.get('ServiceOwnerId')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

