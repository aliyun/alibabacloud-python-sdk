# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCasterLayoutResponseBody(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        layout_id: str = None,
        request_id: str = None,
    ):
        # The ID of the production studio. You can use the ID as a request parameter in the API operation that is used to modify a layout in the production studio, query layouts in the production studio, add a component in the production studio, or query components in the production studio.
        self.caster_id = caster_id
        # The ID of the layout. You can use the ID as a request parameter in the API operation that is used to query layouts in the production studio.
        self.layout_id = layout_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

