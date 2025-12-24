# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class CreateCasterRequest(DaraModel):
    def __init__(
        self,
        caster_name: str = None,
        caster_template: str = None,
        charge_type: str = None,
        client_token: str = None,
        expire_time: str = None,
        norm_type: int = None,
        owner_id: int = None,
        purchase_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateCasterRequestTag] = None,
    ):
        # The name of the production studio.
        self.caster_name = caster_name
        # The preset resolution of the production studio. If the subscription billing method is used, this parameter supports the following valid values:
        # 
        # *   **lp_ld**: low definition
        # *   **lp_sd**: standard definition
        # *   **lp_hd**: high definition
        # *   **lp_ud**: ultra high definition
        # *   **lp_ld_v**: low definition (portrait mode)
        # *   **lp_sd_v**: standard definition (portrait mode)
        # *   **lp_hd_v**: high definition (portrait mode)
        # *   **lp_ud_v**: ultra high definition (portrait mode)
        # 
        # >  If the pay-as-you-go billing method is used, you must call the [SetCasterConfig](https://help.aliyun.com/document_detail/60271.html) operation to specify the resolution.
        self.caster_template = caster_template
        # The billing method. Only the pay-as-you-go billing method is supported.**** Valid values:
        # 
        # *   **PrePaid**: subscription. This billing method is not yet supported.
        # *   **PostPaid**: pay-as-you-go
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can specify a custom value for this parameter, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The expiration time of the production studio. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  This parameter is valid only if you set the **ChargeType** parameter to **PrePaid**.
        self.expire_time = expire_time
        # The type of the production studio. Valid values:
        # 
        # *   **1**: general mode
        # *   **6**: playlist mode (for carousel playback)
        # 
        # This parameter is required.
        self.norm_type = norm_type
        self.owner_id = owner_id
        # The time when the production studio was purchased. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  This parameter is valid only if you set the **ChargeType** parameter to **PrePaid**.
        self.purchase_time = purchase_time
        self.region_id = region_id
        # The ID of the resource group. For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_name is not None:
            result['CasterName'] = self.caster_name

        if self.caster_template is not None:
            result['CasterTemplate'] = self.caster_template

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.norm_type is not None:
            result['NormType'] = self.norm_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.purchase_time is not None:
            result['PurchaseTime'] = self.purchase_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterName') is not None:
            self.caster_name = m.get('CasterName')

        if m.get('CasterTemplate') is not None:
            self.caster_template = m.get('CasterTemplate')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('NormType') is not None:
            self.norm_type = m.get('NormType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PurchaseTime') is not None:
            self.purchase_time = m.get('PurchaseTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateCasterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateCasterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

