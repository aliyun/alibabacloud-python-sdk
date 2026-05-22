# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetSiteResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        site_model: main_models.GetSiteResponseBodySiteModel = None,
    ):
        self.request_id = request_id
        self.site_model = site_model

    def validate(self):
        if self.site_model:
            self.site_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_model is not None:
            result['SiteModel'] = self.site_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteModel') is not None:
            temp_model = main_models.GetSiteResponseBodySiteModel()
            self.site_model = temp_model.from_map(m.get('SiteModel'))

        return self

class GetSiteResponseBodySiteModel(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        cname_zone: str = None,
        coverage: str = None,
        create_time: str = None,
        instance_id: str = None,
        name_server_list: str = None,
        offline_reason: str = None,
        plan_name: str = None,
        plan_spec_name: str = None,
        resource_group_id: str = None,
        site_id: int = None,
        site_name: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        update_time: str = None,
        vanity_nslist: Dict[str, str] = None,
        verify_code: str = None,
        version_management: bool = None,
    ):
        self.access_type = access_type
        self.cname_zone = cname_zone
        self.coverage = coverage
        self.create_time = create_time
        self.instance_id = instance_id
        self.name_server_list = name_server_list
        self.offline_reason = offline_reason
        self.plan_name = plan_name
        self.plan_spec_name = plan_spec_name
        self.resource_group_id = resource_group_id
        self.site_id = site_id
        self.site_name = site_name
        self.status = status
        self.tags = tags
        self.update_time = update_time
        self.vanity_nslist = vanity_nslist
        self.verify_code = verify_code
        self.version_management = version_management

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.cname_zone is not None:
            result['CnameZone'] = self.cname_zone

        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name_server_list is not None:
            result['NameServerList'] = self.name_server_list

        if self.offline_reason is not None:
            result['OfflineReason'] = self.offline_reason

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_spec_name is not None:
            result['PlanSpecName'] = self.plan_spec_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vanity_nslist is not None:
            result['VanityNSList'] = self.vanity_nslist

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        if self.version_management is not None:
            result['VersionManagement'] = self.version_management

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('CnameZone') is not None:
            self.cname_zone = m.get('CnameZone')

        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NameServerList') is not None:
            self.name_server_list = m.get('NameServerList')

        if m.get('OfflineReason') is not None:
            self.offline_reason = m.get('OfflineReason')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanSpecName') is not None:
            self.plan_spec_name = m.get('PlanSpecName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VanityNSList') is not None:
            self.vanity_nslist = m.get('VanityNSList')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        if m.get('VersionManagement') is not None:
            self.version_management = m.get('VersionManagement')

        return self

