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
        enable_auth_free_read: bool = None,
        enable_auth_free_write: bool = None,
        enable_auth_token: bool = None,
        payment_type: str = None,
        prometheus_instance_name: str = None,
        status: str = None,
        storage_duration: int = None,
        workspace: str = None,
    ):
        # The number of days to store archived data after the storage duration expires. A value of 0 disables archiving. For V1 instances, the valid values are 1 to 365. This is supported only for the pay-by-data-write billing method. For V2 instances, the valid values are 1 to 3650. A value of 3650 indicates permanent storage.
        self.archive_duration = archive_duration
        # The policy for password-free read access. The policy supports IP address segments and VPC IDs.
        self.auth_free_read_policy = auth_free_read_policy
        # The policy for password-free write access. The policy supports IP address segments and VPC IDs.
        self.auth_free_write_policy = auth_free_write_policy
        # Specifies whether to enable password-free read access.
        self.enable_auth_free_read = enable_auth_free_read
        # Specifies whether to enable password-free write access.
        self.enable_auth_free_write = enable_auth_free_write
        # Specifies whether to enable authentication with an access token.
        self.enable_auth_token = enable_auth_token
        # The billing method. You can change the billing method only once during the instance lifecycle. Valid values: \\`POSTPAY\\` (pay-as-you-go based on reported metrics) and \\`POSTPAY_GB\\` (pay-as-you-go based on data writes).
        self.payment_type = payment_type
        # The name of the instance.
        self.prometheus_instance_name = prometheus_instance_name
        # The status of the instance storage database. Only RUNNING is supported. If this parameter is left empty, the status of the storage database is not changed.
        self.status = status
        # The storage duration in days. If the instance is billed by data writes, valid values are 90 and 180. If the instance is billed by reported metrics, valid values are 15, 30, 60, 90, and 180.
        self.storage_duration = storage_duration
        # The workspace to which the instance belongs.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_duration is not None:
            result['archiveDuration'] = self.archive_duration

        if self.auth_free_read_policy is not None:
            result['authFreeReadPolicy'] = self.auth_free_read_policy

        if self.auth_free_write_policy is not None:
            result['authFreeWritePolicy'] = self.auth_free_write_policy

        if self.enable_auth_free_read is not None:
            result['enableAuthFreeRead'] = self.enable_auth_free_read

        if self.enable_auth_free_write is not None:
            result['enableAuthFreeWrite'] = self.enable_auth_free_write

        if self.enable_auth_token is not None:
            result['enableAuthToken'] = self.enable_auth_token

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name

        if self.status is not None:
            result['status'] = self.status

        if self.storage_duration is not None:
            result['storageDuration'] = self.storage_duration

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('archiveDuration') is not None:
            self.archive_duration = m.get('archiveDuration')

        if m.get('authFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('authFreeReadPolicy')

        if m.get('authFreeWritePolicy') is not None:
            self.auth_free_write_policy = m.get('authFreeWritePolicy')

        if m.get('enableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('enableAuthFreeRead')

        if m.get('enableAuthFreeWrite') is not None:
            self.enable_auth_free_write = m.get('enableAuthFreeWrite')

        if m.get('enableAuthToken') is not None:
            self.enable_auth_token = m.get('enableAuthToken')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('storageDuration') is not None:
            self.storage_duration = m.get('storageDuration')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

