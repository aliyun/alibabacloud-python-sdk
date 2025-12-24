# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLaunchTemplateDefaultVersionResponseBody(DaraModel):
    def __init__(
        self,
        launch_template_id: str = None,
        request_id: str = None,
    ):
        # The ID of the launch template. For more information, see [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html).
        self.launch_template_id = launch_template_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

