# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateMountTargetResponseBody(DaraModel):
    def __init__(
        self,
        mount_target_domain: str = None,
        mount_target_extra: main_models.CreateMountTargetResponseBodyMountTargetExtra = None,
        request_id: str = None,
    ):
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The information about the mount target.
        self.mount_target_extra = mount_target_extra
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mount_target_extra:
            self.mount_target_extra.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.mount_target_extra is not None:
            result['MountTargetExtra'] = self.mount_target_extra.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('MountTargetExtra') is not None:
            temp_model = main_models.CreateMountTargetResponseBodyMountTargetExtra()
            self.mount_target_extra = temp_model.from_map(m.get('MountTargetExtra'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateMountTargetResponseBodyMountTargetExtra(DaraModel):
    def __init__(
        self,
        dual_stack_mount_target_domain: str = None,
    ):
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')

        return self

