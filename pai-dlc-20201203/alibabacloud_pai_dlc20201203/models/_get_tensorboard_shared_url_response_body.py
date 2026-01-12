# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTensorboardSharedUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboard_shared_url: str = None,
    ):
        # The request ID which is used for troubleshooting.
        self.request_id = request_id
        # The shareable link of the TensorBoard task.
        self.tensorboard_shared_url = tensorboard_shared_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tensorboard_shared_url is not None:
            result['TensorboardSharedUrl'] = self.tensorboard_shared_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TensorboardSharedUrl') is not None:
            self.tensorboard_shared_url = m.get('TensorboardSharedUrl')

        return self

