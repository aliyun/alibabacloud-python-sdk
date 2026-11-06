# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceModifyPriceRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        # The total number of subscription resource nodes after the scale-out. Unit: nodes.
        # 
        # **The value must be greater than the current number of purchased nodes in the delivery group and cannot exceed the node quota of the account.** This parameter is not the number of added nodes or the number of sessions.
        # 
        # For example, if there is currently 1 node and you want to scale out to 2 nodes, specify 2 to indicate a final total of 2 nodes.
        # 
        # This parameter is required.
        self.amount = amount
        # The ID of the delivery group to be scaled out. You can query only one delivery group at a time.
        # 
        # The delivery group must belong to the current account and match ProductType. It must be billed by node on a subscription basis, have a normal order status, and be associated with a resource node pool.
        # 
        # You can obtain the cloud app delivery group ID by calling [ListAppInstanceGroup](https://api.aliyun.com/document/appstream-center/2021-09-01/ListAppInstanceGroup). You can call [GetAppInstanceGroup](https://api.aliyun.com/document/appstream-center/2021-09-01/GetAppInstanceGroup) to further verify the current configuration.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The product type, which must match the product to which the target delivery group belongs. Valid values:
        # 
        # - CloudApp: WUYING Cloud App. Queries the resource scale-out price of a cloud app delivery group.
        # - CloudBrowser: Cloud Browser. Applies only to subscription browser delivery groups that are billed by node.
        # 
        # This operation does not apply to pay-as-you-go or browser groups billed by monthly active user (MAU).
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

