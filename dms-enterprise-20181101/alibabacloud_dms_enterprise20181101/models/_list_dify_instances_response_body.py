# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDifyInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        root: main_models.ListDifyInstancesResponseBodyRoot = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.ListDifyInstancesResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDifyInstancesResponseBodyRoot(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDifyInstancesResponseBodyRootData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDifyInstancesResponseBodyRootData()
                self.data.append(temp_model.from_map(k1))

        return self

class ListDifyInstancesResponseBodyRootData(DaraModel):
    def __init__(
        self,
        app_uuid: str = None,
        created_time: str = None,
        edition: str = None,
        enterprise_internet_url: str = None,
        enterprise_intranet_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_url: str = None,
        intranet_url: str = None,
        major_version: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.app_uuid = app_uuid
        self.created_time = created_time
        self.edition = edition
        self.enterprise_internet_url = enterprise_internet_url
        self.enterprise_intranet_url = enterprise_intranet_url
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.internet_url = internet_url
        self.intranet_url = intranet_url
        self.major_version = major_version
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.workspace_id = workspace_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_uuid is not None:
            result['AppUuid'] = self.app_uuid

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enterprise_internet_url is not None:
            result['EnterpriseInternetUrl'] = self.enterprise_internet_url

        if self.enterprise_intranet_url is not None:
            result['EnterpriseIntranetUrl'] = self.enterprise_intranet_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_url is not None:
            result['InternetUrl'] = self.internet_url

        if self.intranet_url is not None:
            result['IntranetUrl'] = self.intranet_url

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUuid') is not None:
            self.app_uuid = m.get('AppUuid')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EnterpriseInternetUrl') is not None:
            self.enterprise_internet_url = m.get('EnterpriseInternetUrl')

        if m.get('EnterpriseIntranetUrl') is not None:
            self.enterprise_intranet_url = m.get('EnterpriseIntranetUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetUrl') is not None:
            self.internet_url = m.get('InternetUrl')

        if m.get('IntranetUrl') is not None:
            self.intranet_url = m.get('IntranetUrl')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

