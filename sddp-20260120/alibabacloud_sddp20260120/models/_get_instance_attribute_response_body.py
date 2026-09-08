# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        current_kernel_version: str = None,
        engine: str = None,
        engine_version: str = None,
        error_code: str = None,
        error_message: str = None,
        kms_encryption_supported: bool = None,
        maintain_end_time: int = None,
        maintain_start_time: int = None,
        request_id: str = None,
        status: str = None,
    ):
        self.current_kernel_version = current_kernel_version
        self.engine = engine
        self.engine_version = engine_version
        self.error_code = error_code
        self.error_message = error_message
        self.kms_encryption_supported = kms_encryption_supported
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.kms_encryption_supported is not None:
            result['KmsEncryptionSupported'] = self.kms_encryption_supported

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('KmsEncryptionSupported') is not None:
            self.kms_encryption_supported = m.get('KmsEncryptionSupported')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

