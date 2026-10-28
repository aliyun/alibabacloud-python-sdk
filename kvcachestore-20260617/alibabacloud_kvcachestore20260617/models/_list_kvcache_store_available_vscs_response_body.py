# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class ListKVCacheStoreAvailableVscsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vscs: List[main_models.ListKVCacheStoreAvailableVscsResponseBodyVscs] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of available VSC resources.
        self.vscs = vscs

    def validate(self):
        if self.vscs:
            for v1 in self.vscs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Vscs'] = []
        if self.vscs is not None:
            for k1 in self.vscs:
                result['Vscs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vscs = []
        if m.get('Vscs') is not None:
            for k1 in m.get('Vscs'):
                temp_model = main_models.ListKVCacheStoreAvailableVscsResponseBodyVscs()
                self.vscs.append(temp_model.from_map(k1))

        return self

class ListKVCacheStoreAvailableVscsResponseBodyVscs(DaraModel):
    def __init__(
        self,
        vsc_id: str = None,
        vsc_status: str = None,
    ):
        # The VSC device ID.
        self.vsc_id = vsc_id
        # The current status of the VSC device.
        self.vsc_status = vsc_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        if self.vsc_status is not None:
            result['VscStatus'] = self.vsc_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        if m.get('VscStatus') is not None:
            self.vsc_status = m.get('VscStatus')

        return self

