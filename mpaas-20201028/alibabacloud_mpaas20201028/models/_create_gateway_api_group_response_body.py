# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class CreateGatewayApiGroupResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        api_group: main_models.CreateGatewayApiGroupResponseBodyApiGroup = None,
        error_field: str = None,
        http_status_code: int = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.api_group = api_group
        self.error_field = error_field
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.api_group:
            self.api_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.api_group is not None:
            result['ApiGroup'] = self.api_group.to_map()

        if self.error_field is not None:
            result['ErrorField'] = self.error_field

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('ApiGroup') is not None:
            temp_model = main_models.CreateGatewayApiGroupResponseBodyApiGroup()
            self.api_group = temp_model.from_map(m.get('ApiGroup'))

        if m.get('ErrorField') is not None:
            self.error_field = m.get('ErrorField')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateGatewayApiGroupResponseBodyApiGroup(DaraModel):
    def __init__(
        self,
        centers: Dict[str, Any] = None,
        description: str = None,
        domain_name: str = None,
        enable_mtls: bool = None,
        group_id: int = None,
        group_name: str = None,
        host: str = None,
        https_model: bool = None,
        instance_id: str = None,
        instance_port: int = None,
        region_mode: bool = None,
        timeout: int = None,
        upstream_type: str = None,
        vpc_id: str = None,
        vpc_model: bool = None,
    ):
        self.centers = centers
        self.description = description
        self.domain_name = domain_name
        self.enable_mtls = enable_mtls
        self.group_id = group_id
        self.group_name = group_name
        self.host = host
        self.https_model = https_model
        self.instance_id = instance_id
        self.instance_port = instance_port
        self.region_mode = region_mode
        self.timeout = timeout
        self.upstream_type = upstream_type
        self.vpc_id = vpc_id
        self.vpc_model = vpc_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.centers is not None:
            result['Centers'] = self.centers

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.enable_mtls is not None:
            result['EnableMTLS'] = self.enable_mtls

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.host is not None:
            result['Host'] = self.host

        if self.https_model is not None:
            result['HttpsModel'] = self.https_model

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port

        if self.region_mode is not None:
            result['RegionMode'] = self.region_mode

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_model is not None:
            result['VpcModel'] = self.vpc_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Centers') is not None:
            self.centers = m.get('Centers')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EnableMTLS') is not None:
            self.enable_mtls = m.get('EnableMTLS')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpsModel') is not None:
            self.https_model = m.get('HttpsModel')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')

        if m.get('RegionMode') is not None:
            self.region_mode = m.get('RegionMode')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcModel') is not None:
            self.vpc_model = m.get('VpcModel')

        return self

