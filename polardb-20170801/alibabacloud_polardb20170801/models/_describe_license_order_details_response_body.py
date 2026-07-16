# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLicenseOrderDetailsResponseBody(DaraModel):
    def __init__(
        self,
        activated_code_count: int = None,
        activation_code_quota: int = None,
        aliyun_order_id: str = None,
        allow_empty_system_identifier: bool = None,
        engine: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        is_virtual_order: bool = None,
        is_virtual_order_frozen: bool = None,
        package_type: str = None,
        package_validity: str = None,
        purchase_channel: str = None,
        request_id: str = None,
        virtual_order_id: str = None,
    ):
        # The number of activation codes that have been generated.
        self.activated_code_count = activated_code_count
        # The quota for requesting activation codes.
        self.activation_code_quota = activation_code_quota
        # The ID of the Alibaba Cloud order, including the virtual order ID.
        self.aliyun_order_id = aliyun_order_id
        # Indicates whether you can leave the System Identifier parameter empty when you generate an activation code.
        self.allow_empty_system_identifier = allow_empty_system_identifier
        # The database type, such as PG, Oracle, or MySQL.
        self.engine = engine
        # The time when the order was created.
        self.gmt_created = gmt_created
        # The time when the order was last updated.
        self.gmt_modified = gmt_modified
        # Indicates whether the order is a virtual order. You can pre-generate activation codes for virtual orders.
        self.is_virtual_order = is_virtual_order
        # Indicates whether the virtual order is frozen. If a virtual order is frozen, you can no longer generate activation codes.
        self.is_virtual_order_frozen = is_virtual_order_frozen
        # The package type. Valid values:
        # 
        # - single_node_subscribe: single-node (subscription)
        # 
        # - single_node_long_term: single-node (long-term)
        # 
        # - primary_backup_subscribe: primary/standby (subscription)
        # 
        # - primary_backup_long_term: primary/standby (long-term)
        # 
        # - pre_generation_long_term: pre-generation (long-term)
        self.package_type = package_type
        # The validity period of the package. The validity period is typically one year or a long-term period of 30 years.
        self.package_validity = package_validity
        # The purchase channel. Valid values: \\`aliyun_market\\` (Alibaba Cloud Marketplace) and \\`aliyun_public\\` (standard purchase page).
        self.purchase_channel = purchase_channel
        # The request ID.
        self.request_id = request_id
        # The virtual order ID.
        self.virtual_order_id = virtual_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated_code_count is not None:
            result['ActivatedCodeCount'] = self.activated_code_count

        if self.activation_code_quota is not None:
            result['ActivationCodeQuota'] = self.activation_code_quota

        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id

        if self.allow_empty_system_identifier is not None:
            result['AllowEmptySystemIdentifier'] = self.allow_empty_system_identifier

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.is_virtual_order is not None:
            result['IsVirtualOrder'] = self.is_virtual_order

        if self.is_virtual_order_frozen is not None:
            result['IsVirtualOrderFrozen'] = self.is_virtual_order_frozen

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_validity is not None:
            result['PackageValidity'] = self.package_validity

        if self.purchase_channel is not None:
            result['PurchaseChannel'] = self.purchase_channel

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.virtual_order_id is not None:
            result['VirtualOrderId'] = self.virtual_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivatedCodeCount') is not None:
            self.activated_code_count = m.get('ActivatedCodeCount')

        if m.get('ActivationCodeQuota') is not None:
            self.activation_code_quota = m.get('ActivationCodeQuota')

        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')

        if m.get('AllowEmptySystemIdentifier') is not None:
            self.allow_empty_system_identifier = m.get('AllowEmptySystemIdentifier')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IsVirtualOrder') is not None:
            self.is_virtual_order = m.get('IsVirtualOrder')

        if m.get('IsVirtualOrderFrozen') is not None:
            self.is_virtual_order_frozen = m.get('IsVirtualOrderFrozen')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageValidity') is not None:
            self.package_validity = m.get('PackageValidity')

        if m.get('PurchaseChannel') is not None:
            self.purchase_channel = m.get('PurchaseChannel')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VirtualOrderId') is not None:
            self.virtual_order_id = m.get('VirtualOrderId')

        return self

