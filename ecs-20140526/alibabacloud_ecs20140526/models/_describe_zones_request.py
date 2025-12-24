# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeZonesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_charge_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spot_strategy: str = None,
        verbose: bool = None,
    ):
        # The natural language that is used to filter responses. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231). Valid values:
        # 
        # *   zh-CN: Simplified Chinese
        # *   zh_TW: Traditional Chinese
        # *   en-US: English
        # *   ja: Japanese
        # *   fr: French
        # *   de: German
        # *   ko: Korean
        # 
        # Default value: zh-CN.
        self.accept_language = accept_language
        # The billing method of resources. For more information, see [Billing overview](https://help.aliyun.com/document_detail/25398.html). Valid values:
        # 
        # *   Prepaid: subscription
        # *   PostPaid: pay-as-you-go
        # 
        # Default value: PostPaid.
        self.instance_charge_type = instance_charge_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The bidding policy for the pay-as-you-go instance. You can specify this parameter when you set `InstanceChargeType` to PostPaid. For more information, see [Spot instances](https://help.aliyun.com/document_detail/52088.html). Valid values:
        # 
        # *   NoSpot: The instances are regular pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instance is a spot instance that has a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is a spot instance for which the market price is automatically used as the bid price. The market price can be up to the pay-as-you-go price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # Specifies whether to display detailed information.
        # 
        # *   true: displays detailed information.
        # *   false: does not display detailed information.
        # 
        # Default value: true.
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

