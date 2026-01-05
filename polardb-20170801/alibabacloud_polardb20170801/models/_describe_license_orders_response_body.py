# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeLicenseOrdersResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeLicenseOrdersResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The queried orders.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeLicenseOrdersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeLicenseOrdersResponseBodyItems(DaraModel):
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
        virtual_aliyun_order_id: str = None,
    ):
        # The number of generated activation codes.
        self.activated_code_count = activated_code_count
        # The maximum number of activation codes that you can apply for.
        self.activation_code_quota = activation_code_quota
        # The ID of the Alibaba Cloud order. The ID of a virtual order may be returned.
        self.aliyun_order_id = aliyun_order_id
        # Indicates whether the SystemIdentifier parameter can be left empty when the system generates an activation code.
        self.allow_empty_system_identifier = allow_empty_system_identifier
        # The engine of the PolarDB cluster. Valid values: PG, Oracle, and MySQL.
        self.engine = engine
        # The time when the order was created.
        self.gmt_created = gmt_created
        # The time when the order was updated.
        self.gmt_modified = gmt_modified
        # Indicates whether the order is a virtual order. Pre-generation of activation codes is allowed for virtual orders.
        self.is_virtual_order = is_virtual_order
        # Indicates whether the virtual order is frozen. Generation of activation codes is not allowed for frozen virtual orders.
        self.is_virtual_order_frozen = is_virtual_order_frozen
        # The type of the package. Valid values:
        # 
        # *   single_node_subscribe: Single-node Edition (Subscription).
        # *   single_node_long_term: Single-node Edition (Long-term).
        # *   primary_backup_subscribe: HA Edition (Subscription).
        # *   primary_backup_long_term: HA Edition (Long-term).
        # *   pre_generation_long_term: Pre-generated (Long-term).
        self.package_type = package_type
        # The validity period of the package. Valid values: 1 year and 30 years.
        self.package_validity = package_validity
        # The purchase channel. Valid values: aliyun_market and aliyun_public. aliyun_market indicates Alibaba Cloud Marketplace. aliyun_public indicates the PolarDB buy page.
        self.purchase_channel = purchase_channel
        # The ID of the virtual order.
        self.virtual_aliyun_order_id = virtual_aliyun_order_id

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

        if self.virtual_aliyun_order_id is not None:
            result['VirtualAliyunOrderId'] = self.virtual_aliyun_order_id

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

        if m.get('VirtualAliyunOrderId') is not None:
            self.virtual_aliyun_order_id = m.get('VirtualAliyunOrderId')

        return self

