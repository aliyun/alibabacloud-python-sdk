# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddVodTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vod_template_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The snapshot or animated image template ID. This ID can be used as a request parameter of the [SubmitSnapshotJob](~~SubmitSnapshotJob~~) or [SubmitDynamicImageJob](~~SubmitDynamicImageJob~~) operation to initiate snapshot or animated image processing.
        self.vod_template_id = vod_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')

        return self

