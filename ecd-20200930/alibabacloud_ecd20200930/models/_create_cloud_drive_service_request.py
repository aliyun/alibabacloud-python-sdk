# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCloudDriveServiceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_type: int = None,
        cds_charge_type: str = None,
        cen_id: str = None,
        domain_name: str = None,
        end_user_id: List[str] = None,
        max_size: int = None,
        name: str = None,
        office_site_id: str = None,
        office_site_type: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        solution_id: str = None,
        user_count: int = None,
        user_max_size: int = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-payment feature. Ensure your Alibaba Cloud account has sufficient balance. Insufficient balance may result in abnormal orders.
        # *   false (default): disables the auto-payment feature. The order is generated, but payment must be made manually. You can log on to the Alibaba Cloud Management Console and complete the payment based on the order ID on the Orders page.
        self.auto_pay = auto_pay
        # Optional. Specifies whether to enable the auto-renewal feature. This parameter takes effect only if you set CdsChargeType to `Prepaid`.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # >  This parameter is not publicly available.
        self.biz_type = biz_type
        # The billing method of the enterprise drive.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        self.cds_charge_type = cds_charge_type
        # The ID of the Cloud Enterprise Network (CEN) instance. This parameter takes effect only if you set `OfficeSiteType` to `AD_CONNECTOR`. If you have configured `OfficeSiteId`, you can leave this parameter empty.
        self.cen_id = cen_id
        # The domain name of the enterprise AD office network. This parameter takes effect only if you set `OfficeSiteType` to `AD_CONNECTOR`. If you have configured `OfficeSiteId`, you can leave this parameter empty.
        self.domain_name = domain_name
        # The user IDs.
        self.end_user_id = end_user_id
        # The maximum storage capacity of the enterprise drive.
        # 
        # *   For a pay-as-you-go enterprise drive, the unit is bytes.
        # *   For a subscription enterprise drive, the unit is GiB. For example, to create a 500 GiB subscription drive, set the value to 500 GiB. To create a 2 TiB subscription drive, set the value to 2048 GiB.
        # 
        # This parameter is required.
        self.max_size = max_size
        # The name of the enterprise drive
        self.name = name
        # The ID of the office network. This parameter takes effect only if you set OfficeSiteType to `AD_CONNECTOR`.
        self.office_site_id = office_site_id
        # The type of the office network.
        # 
        # Valid values:
        # 
        # *   SIMPLE: convenience office network.
        # *   AD_CONNECTOR: enterprise Active Directory (AD) office network.
        self.office_site_type = office_site_type
        # The subscription duration. The unit is specified by `PeriodUnit`. This parameter takes effect only if you set `CdsChargeType` to `PrePaid`.
        # 
        # Valid values:
        # 
        # *   1
        # *   2
        # *   3
        self.period = period
        # Required. The unit of the subscription duration. This parameter takes effect only if you set `CdsChargeType` to `PrePaid`.
        # 
        # Valid value:
        # 
        # *   Year
        self.period_unit = period_unit
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Enterprise Drive Service is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # >  This parameter is not publicly available.
        self.solution_id = solution_id
        # Required. The maximum number of users allowed on the enterprise drive. This parameter takes effect only if you set `CdsChargeType` to `PrePaid`.
        # 
        # Valid values:
        # 
        # *   5 when the value of MaxSize is 500 GiB.
        # *   20 when the value of MaxSize is 2048 GiB.
        # *   50 when the value of MaxSize is 5120 GiB.
        self.user_count = user_count
        # The maximum storage capacity of the user\\"s personal disk when allocated. Unit: bytes.
        self.user_max_size = user_max_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.cds_charge_type is not None:
            result['CdsChargeType'] = self.cds_charge_type

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.max_size is not None:
            result['MaxSize'] = self.max_size

        if self.name is not None:
            result['Name'] = self.name

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        if self.user_max_size is not None:
            result['UserMaxSize'] = self.user_max_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CdsChargeType') is not None:
            self.cds_charge_type = m.get('CdsChargeType')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        if m.get('UserMaxSize') is not None:
            self.user_max_size = m.get('UserMaxSize')

        return self

