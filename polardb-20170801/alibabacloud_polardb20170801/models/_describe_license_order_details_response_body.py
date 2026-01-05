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
        # The number of generated activation codes.
        self.activated_code_count = activated_code_count
        # The maximum number of activation codes that you can apply for.
        self.activation_code_quota = activation_code_quota
        # The Alibaba Cloud order ID (including the virtual order ID).
        self.aliyun_order_id = aliyun_order_id
        # Indicates whether activation codes can be generated without the system identifier.
        self.allow_empty_system_identifier = allow_empty_system_identifier
        # The type of the engine. Valid values: PG, Oracle, and MySQL.
        self.engine = engine
        # The time when the order was created.
        self.gmt_created = gmt_created
        # The time when the order was last updated.
        self.gmt_modified = gmt_modified
        # Indicates whether the order is a virtual order (virtual orders allow pre-generation of activation codes).
        self.is_virtual_order = is_virtual_order
        # Indicates whether the virtual order is frozen (activation codes cannot be generated for a frozen virtual order).
        self.is_virtual_order_frozen = is_virtual_order_frozen
        # The plan type. Valid values:
        # 
        # *   single_node_subscribe
        # *   single_node_long_term
        # *   primary_backup_subscribe
        # *   primary_backup_long_term
        # *   pre_generation_long_term
        self.package_type = package_type
        # The validity period of the plan, which is one year (common) or thirty years (long-term).
        self.package_validity = package_validity
        # The plan validity period, one year (common) or thirty years (long-term).
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

