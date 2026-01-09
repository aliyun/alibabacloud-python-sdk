# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EncryptUserCmkConf(DaraModel):
    def __init__(
        self,
        arn: str = None,
        cmk_key_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.arn = arn
        # This parameter is required.
        self.cmk_key_id = cmk_key_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['arn'] = self.arn

        if self.cmk_key_id is not None:
            result['cmk_key_id'] = self.cmk_key_id

        if self.region_id is not None:
            result['region_id'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')

        if m.get('cmk_key_id') is not None:
            self.cmk_key_id = m.get('cmk_key_id')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        return self

