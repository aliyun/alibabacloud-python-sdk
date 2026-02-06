# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteTranscodeTemplateGroupResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_transcode_template_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of transcoding templates that were not found.
        self.non_exist_transcode_template_ids = non_exist_transcode_template_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_transcode_template_ids is not None:
            result['NonExistTranscodeTemplateIds'] = self.non_exist_transcode_template_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistTranscodeTemplateIds') is not None:
            self.non_exist_transcode_template_ids = m.get('NonExistTranscodeTemplateIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

