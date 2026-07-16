# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSupportResourceTypesRequest(DaraModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        product_code: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_tye: str = None,
        show_items: bool = None,
        support_code: str = None,
    ):
        # The number of entries to return on each page.
        # 
        # Maximum value: 1000. Default value: 50.
        self.max_result = max_result
        # The token that is used to start the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The service code. This parameter specifies a filter condition for the query.
        # 
        # This parameter is obtained from the response.
        self.product_code = product_code
        # The region ID.
        # 
        # For more information about region IDs, see [Endpoints](https://help.aliyun.com/document_detail/2330902.html).
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The resource type. This parameter specifies a filter condition for the query.
        # 
        # This parameter is obtained from the response.
        self.resource_tye = resource_tye
        # Specifies whether to return tag-related capability items. Valid values:
        # 
        # *   true: The system returns tag-related capability items.
        # *   false (default value): The system does not return tag-related capability items.
        self.show_items = show_items
        # The code of the tag-related capability item. This parameter specifies a filter condition for the query.
        # 
        # For more information, see **Tag-related capability items**.
        self.support_code = support_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_result is not None:
            result['MaxResult'] = self.max_result

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_tye is not None:
            result['ResourceTye'] = self.resource_tye

        if self.show_items is not None:
            result['ShowItems'] = self.show_items

        if self.support_code is not None:
            result['SupportCode'] = self.support_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceTye') is not None:
            self.resource_tye = m.get('ResourceTye')

        if m.get('ShowItems') is not None:
            self.show_items = m.get('ShowItems')

        if m.get('SupportCode') is not None:
            self.support_code = m.get('SupportCode')

        return self

