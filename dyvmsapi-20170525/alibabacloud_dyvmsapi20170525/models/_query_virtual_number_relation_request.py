# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVirtualNumberRelationRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_num: str = None,
        prod_code: str = None,
        qualification_id: int = None,
        region_name_city: str = None,
        related_num: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_type: int = None,
        spec_id: int = None,
    ):
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The virtual number.
        self.phone_num = phone_num
        # The service name. Default value: **dyvms**.
        self.prod_code = prod_code
        # The qualification ID.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Qualifications\\&Communication Scripts > Qualification Management**, and then click **Details** in the Actions column to view the qualification ID.
        self.qualification_id = qualification_id
        # The city to which the virtual number belongs.
        self.region_name_city = region_name_city
        # The real number.
        self.related_num = related_num
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route type. Valid values:
        # 
        # **0**: number location first. **1**: random.
        self.route_type = route_type
        # The number type. Valid values:
        # 
        # *   **1**: the number provided by a virtual network operator, in the 05710000\\*\\*\\*\\* format.
        # *   **2**: the number provided by an Internet service provider (ISP).
        # *   **3**: a 5-digit phone number that starts with 95.
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.region_name_city is not None:
            result['RegionNameCity'] = self.region_name_city

        if self.related_num is not None:
            result['RelatedNum'] = self.related_num

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('RegionNameCity') is not None:
            self.region_name_city = m.get('RegionNameCity')

        if m.get('RelatedNum') is not None:
            self.related_num = m.get('RelatedNum')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        return self

