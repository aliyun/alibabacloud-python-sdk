# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePrometheusInstanceRequest(DaraModel):
    def __init__(
        self,
        archive_duration: int = None,
        auth_free_read_policy: str = None,
        auth_free_write_policy: str = None,
        cluster_id: str = None,
        enable_auth_free_read: bool = None,
        enable_auth_free_write: bool = None,
        enable_auth_token: bool = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_duration: int = None,
    ):
        # The number of days for which data is automatically archived after the storage expires. Valid values: 60, 90, 180, and 365. 0 indicates that the data is not archived.
        self.archive_duration = archive_duration
        # The IP addresses or CIDR blocks for which password-free read is enabled. Separate multiple IP addresses with line breaks.
        self.auth_free_read_policy = auth_free_read_policy
        # The IP addresses or CIDR blocks for which password-free write is enabled. Separate multiple IP addresses with line breaks.
        self.auth_free_write_policy = auth_free_write_policy
        # The ID of the Prometheus instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to enable password-free read.
        self.enable_auth_free_read = enable_auth_free_read
        # Specifies whether to enable password-free write.
        self.enable_auth_free_write = enable_auth_free_write
        # Specifies whether to enable access token authentication.
        self.enable_auth_token = enable_auth_token
        # The billing mode. Valid values: POSTPAY: charges fees based on the amount of reported metric data. POSTPAY_GB: charges fees based on the amount of written metric data.
        self.payment_type = payment_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Prometheus resource group.
        self.resource_group_id = resource_group_id
        # The data storage duration. Unit: days.
        self.storage_duration = storage_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_duration is not None:
            result['ArchiveDuration'] = self.archive_duration

        if self.auth_free_read_policy is not None:
            result['AuthFreeReadPolicy'] = self.auth_free_read_policy

        if self.auth_free_write_policy is not None:
            result['AuthFreeWritePolicy'] = self.auth_free_write_policy

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.enable_auth_free_read is not None:
            result['EnableAuthFreeRead'] = self.enable_auth_free_read

        if self.enable_auth_free_write is not None:
            result['EnableAuthFreeWrite'] = self.enable_auth_free_write

        if self.enable_auth_token is not None:
            result['EnableAuthToken'] = self.enable_auth_token

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage_duration is not None:
            result['StorageDuration'] = self.storage_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDuration') is not None:
            self.archive_duration = m.get('ArchiveDuration')

        if m.get('AuthFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('AuthFreeReadPolicy')

        if m.get('AuthFreeWritePolicy') is not None:
            self.auth_free_write_policy = m.get('AuthFreeWritePolicy')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EnableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('EnableAuthFreeRead')

        if m.get('EnableAuthFreeWrite') is not None:
            self.enable_auth_free_write = m.get('EnableAuthFreeWrite')

        if m.get('EnableAuthToken') is not None:
            self.enable_auth_token = m.get('EnableAuthToken')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StorageDuration') is not None:
            self.storage_duration = m.get('StorageDuration')

        return self

