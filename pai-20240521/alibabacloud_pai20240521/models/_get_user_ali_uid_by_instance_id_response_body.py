# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserAliUidByInstanceIdResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        code: str = None,
        cpus: int = None,
        create_time: int = None,
        intranet_ip: str = None,
        memory: int = None,
        message: str = None,
        namespace_id: str = None,
        pod_name: str = None,
        pod_uid: str = None,
        request_id: str = None,
        resouce_type: str = None,
        resource_instance_id: str = None,
        status: str = None,
        update_time: int = None,
        user_uid: str = None,
    ):
        self.application_id = application_id
        self.application_name = application_name
        self.code = code
        self.cpus = cpus
        self.create_time = create_time
        self.intranet_ip = intranet_ip
        self.memory = memory
        self.message = message
        self.namespace_id = namespace_id
        self.pod_name = pod_name
        self.pod_uid = pod_uid
        self.request_id = request_id
        self.resouce_type = resouce_type
        self.resource_instance_id = resource_instance_id
        self.status = status
        self.update_time = update_time
        self.user_uid = user_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.code is not None:
            result['Code'] = self.code

        if self.cpus is not None:
            result['Cpus'] = self.cpus

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resouce_type is not None:
            result['ResouceType'] = self.resouce_type

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_uid is not None:
            result['UserUid'] = self.user_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Cpus') is not None:
            self.cpus = m.get('Cpus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResouceType') is not None:
            self.resouce_type = m.get('ResouceType')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')

        return self

