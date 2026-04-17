# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class DescribeAclsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        kafka_acl_list: main_models.DescribeAclsResponseBodyKafkaAclList = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        self.kafka_acl_list = kafka_acl_list
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.kafka_acl_list:
            self.kafka_acl_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.kafka_acl_list is not None:
            result['KafkaAclList'] = self.kafka_acl_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('KafkaAclList') is not None:
            temp_model = main_models.DescribeAclsResponseBodyKafkaAclList()
            self.kafka_acl_list = temp_model.from_map(m.get('KafkaAclList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAclsResponseBodyKafkaAclList(DaraModel):
    def __init__(
        self,
        kafka_acl_vo: List[main_models.DescribeAclsResponseBodyKafkaAclListKafkaAclVO] = None,
    ):
        self.kafka_acl_vo = kafka_acl_vo

    def validate(self):
        if self.kafka_acl_vo:
            for v1 in self.kafka_acl_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KafkaAclVO'] = []
        if self.kafka_acl_vo is not None:
            for k1 in self.kafka_acl_vo:
                result['KafkaAclVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kafka_acl_vo = []
        if m.get('KafkaAclVO') is not None:
            for k1 in m.get('KafkaAclVO'):
                temp_model = main_models.DescribeAclsResponseBodyKafkaAclListKafkaAclVO()
                self.kafka_acl_vo.append(temp_model.from_map(k1))

        return self

class DescribeAclsResponseBodyKafkaAclListKafkaAclVO(DaraModel):
    def __init__(
        self,
        acl_operation_type: str = None,
        acl_permission_type: str = None,
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        username: str = None,
    ):
        self.acl_operation_type = acl_operation_type
        self.acl_permission_type = acl_permission_type
        self.acl_resource_name = acl_resource_name
        self.acl_resource_pattern_type = acl_resource_pattern_type
        self.acl_resource_type = acl_resource_type
        self.host = host
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type

        if self.acl_permission_type is not None:
            result['AclPermissionType'] = self.acl_permission_type

        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name

        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type

        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type

        if self.host is not None:
            result['Host'] = self.host

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')

        if m.get('AclPermissionType') is not None:
            self.acl_permission_type = m.get('AclPermissionType')

        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')

        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')

        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

