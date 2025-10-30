# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStreamingDataServiceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        request_id: str = None,
        service_description: str = None,
        service_id: str = None,
        service_ip: str = None,
        service_managed: bool = None,
        service_name: str = None,
        service_owner_id: str = None,
        service_port: int = None,
        service_spec: str = None,
        status: str = None,
    ):
        # The time when the service was created.
        self.create_time = create_time
        # The time when the service was last modified.
        self.modify_time = modify_time
        # The request ID.
        self.request_id = request_id
        # The description of the service.
        self.service_description = service_description
        # The service ID.
        self.service_id = service_id
        # The IP address of the service.
        self.service_ip = service_ip
        # The service is managed by other aliyun product or not.
        self.service_managed = service_managed
        # The name of the service.
        self.service_name = service_name
        # The service account uid of the aliyun product
        self.service_owner_id = service_owner_id
        # The port number of the service.
        self.service_port = service_port
        # The specifications of the service.
        self.service_spec = service_spec
        # The status of the service. Valid values:
        # 
        # *   Init
        # *   Running
        # *   Exception
        # *   Paused
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

