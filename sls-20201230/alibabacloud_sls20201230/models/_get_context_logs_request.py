# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContextLogsRequest(DaraModel):
    def __init__(
        self,
        back_lines: int = None,
        forward_lines: int = None,
        pack_id: str = None,
        pack_meta: str = None,
    ):
        # The number of logs that you want to obtain and are generated before the generation time of the start log. Valid values: `(0,100]`.
        # 
        # This parameter is required.
        self.back_lines = back_lines
        # The number of logs that you want to obtain and are generated after the generation time of the start log. Valid values: `(0,100]`.
        # 
        # This parameter is required.
        self.forward_lines = forward_lines
        # The unique identifier of the log group to which the start log belongs.
        # 
        # This parameter is required.
        self.pack_id = pack_id
        # The unique context identifier of the start log in the log group.
        # 
        # This parameter is required.
        self.pack_meta = pack_meta

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_lines is not None:
            result['back_lines'] = self.back_lines

        if self.forward_lines is not None:
            result['forward_lines'] = self.forward_lines

        if self.pack_id is not None:
            result['pack_id'] = self.pack_id

        if self.pack_meta is not None:
            result['pack_meta'] = self.pack_meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('back_lines') is not None:
            self.back_lines = m.get('back_lines')

        if m.get('forward_lines') is not None:
            self.forward_lines = m.get('forward_lines')

        if m.get('pack_id') is not None:
            self.pack_id = m.get('pack_id')

        if m.get('pack_meta') is not None:
            self.pack_meta = m.get('pack_meta')

        return self

