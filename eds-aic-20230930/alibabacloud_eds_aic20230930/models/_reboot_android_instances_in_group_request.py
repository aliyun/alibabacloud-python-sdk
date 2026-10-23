# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RebootAndroidInstancesInGroupRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        force_stop: bool = None,
        ignore_param_validation: bool = None,
        sale_mode: str = None,
    ):
        # The list of instance IDs.
        self.android_instance_ids = android_instance_ids
        # Specifies whether to force a restart. You can force a restart if a cloud phone cannot be shut down due to system or network exceptions. Unsaved data may be lost.
        self.force_stop = force_stop
        # Specifies whether to skip parameter validation. A value of true indicates that validation is skipped. If the value is false or not specified, validation is performed.
        self.ignore_param_validation = ignore_param_validation
        # **[Deprecated]** The sales mode.
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.ignore_param_validation is not None:
            result['IgnoreParamValidation'] = self.ignore_param_validation

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('IgnoreParamValidation') is not None:
            self.ignore_param_validation = m.get('IgnoreParamValidation')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        return self

