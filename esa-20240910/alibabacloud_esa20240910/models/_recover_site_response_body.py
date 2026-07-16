# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecoverSiteResponseBody(DaraModel):
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
        request_id: str = None,
        resource_group_id: str = None,
        site_id: int = None,
        site_name: str = None,
        status: str = None,
        update_time: str = None,
        verify_code: str = None,
    ):
        # The access type. Valid values:
        # 
        # - **NS**: access through NS hosting.
        # 
        # - **CNAME**: access through CNAME.
        self.access_type = access_type
        # The CNAME suffix of the site. For sites accessed through CNAME, this is the suffix that needs to be configured for the CNAME record.
        self.cname_zone = cname_zone
        # The acceleration region of the site. Valid values:
        # - **domestic**: the Chinese mainland only.
        # - **global**: global.
        # - **overseas**: global (excluding the Chinese mainland).
        self.coverage = coverage
        # The creation time.
        self.create_time = create_time
        # The plan instance ID.
        self.instance_id = instance_id
        # The list of name servers assigned to the site, separated by commas (,). When the site is accessed through NS, this field contains values. You need to change the DNS servers of the site to these name servers. Then you can verify site ownership and activate the site.
        self.name_server_list = name_server_list
        # The reason why the site was disabled. Valid values:
        # 
        # - **expiration_ arrears**: the subscription plan expired or the account has an overdue payment.
        # - **internally_disabled**: disabled by the system internally.
        # - **missing_icp**: the domain name lacks an ICP filing.
        # - **content_violation**: content violation.
        # - **proactively_disabled**: you proactively disabled the site or the site was disabled due to the usage cap you configured.
        self.offline_reason = offline_reason
        # The plan name.
        self.plan_name = plan_name
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The site ID.
        self.site_id = site_id
        # The site name.
        self.site_name = site_name
        # The site status. Valid values:
        # 
        # - **pending**: the site is pending configuration.
        # - **active**: the site is activated.
        # - **offline**: the site is offline.
        # - **moved**: the site has been superseded.
        self.status = status
        # The modification time.
        self.update_time = update_time
        # The site ownership verification code. When the site is accessed through CNAME, this is the TXT verification code that needs to be configured.
        self.verify_code = verify_code

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        return self

