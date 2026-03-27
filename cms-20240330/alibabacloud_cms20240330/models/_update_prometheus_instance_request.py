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
        # The number of days to automatically archive and save after the storage expires, 0 means no archiving. The range of archiving days:
        # V1: 1~365 days. Only supported for metric write volume.
        # V2: 1~3650 days (3650 indicates permanent storage).
        self.archive_duration = archive_duration
        # Password-free read policy (supports IP segments and VpcId).
        self.auth_free_read_policy = auth_free_read_policy
        # Password-free write policy (supports IP segments and VpcId).
        self.auth_free_write_policy = auth_free_write_policy
        # Whether to enable password-free read.
        self.enable_auth_free_read = enable_auth_free_read
        # Whether to enable password-free write.
        self.enable_auth_free_write = enable_auth_free_write
        # Whether to enable access token authentication.
        self.enable_auth_token = enable_auth_token
        # Billing method (can only be modified once during the instance\\"s lifecycle):
        # POSTPAY: Postpaid by metric reporting volume.
        # POSTPAY_GB: Postpaid by metric write volume.
        self.payment_type = payment_type
        # Instance name.
        self.prometheus_instance_name = prometheus_instance_name
        # Instance storage DB status (only supports RUNNING). If empty, the storage DB status will not be changed.
        self.status = status
        # Storage duration (days):
        # By write volume: 90, 180.
        # By metric reporting volume: 15, 30, 60, 90, 180.
        self.storage_duration = storage_duration
        # Belonging workspace.
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

