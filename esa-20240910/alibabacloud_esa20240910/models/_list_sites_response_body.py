# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListSitesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sites: List[main_models.ListSitesResponseBodySites] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of websites per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried websites.
        self.sites = sites
        # The total number of websites.
        self.total_count = total_count

    def validate(self):
        if self.sites:
            for v1 in self.sites:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sites'] = []
        if self.sites is not None:
            for k1 in self.sites:
                result['Sites'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sites = []
        if m.get('Sites') is not None:
            for k1 in m.get('Sites'):
                temp_model = main_models.ListSitesResponseBodySites()
                self.sites.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSitesResponseBodySites(DaraModel):
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
        verify_code: str = None,
        visit_time: str = None,
    ):
        # The DNS setup for the website. Valid values:
        # 
        # *   **NS**
        # *   **CNAME**
        self.access_type = access_type
        # The CNAME of the website domain. If you use CNAME setup when you add your website to ESA, the value is the CNAME that you configured then.
        self.cname_zone = cname_zone
        # The service location for the website. Valid values:
        # 
        # *   **domestic**: the Chinese mainland
        # *   **global**: global
        # *   **overseas**: outside the Chinese mainland
        self.coverage = coverage
        # The time when the website was added. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the plan associated with the website.
        self.instance_id = instance_id
        # The nameservers assigned to the website domain, which are separated by commas (,).
        self.name_server_list = name_server_list
        self.offline_reason = offline_reason
        # The plan name.
        self.plan_name = plan_name
        # The plan associated with the website.
        self.plan_spec_name = plan_spec_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name
        # The website status. Valid values:
        # 
        # *   **pending**: The website is to be configured.
        # *   **active**: The website is active.
        # *   **offline**: The website is suspended.
        # *   **moved**: The website has been added and verified by another Alibaba Cloud account.
        self.status = status
        # The tags of the website.
        self.tags = tags
        # The time when the website was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The code that is used to verify the website domain ownership. As part of the verification TXT record, this parameter is returned for websites that use CNAME setup.
        self.verify_code = verify_code
        # The website visit time is represented in the ISO 8601 date format using UTC time, formatted as yyyy-MM-ddTHH:mm:ssZ.
        self.visit_time = visit_time

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

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        if self.visit_time is not None:
            result['VisitTime'] = self.visit_time

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

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        if m.get('VisitTime') is not None:
            self.visit_time = m.get('VisitTime')

        return self

