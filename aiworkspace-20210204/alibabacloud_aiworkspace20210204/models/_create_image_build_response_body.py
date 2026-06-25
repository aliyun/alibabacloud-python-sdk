# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageBuildResponseBody(DaraModel):
    def __init__(
        self,
        image_build_id: str = None,
        image_build_job_id: str = None,
    ):
        # The image build ID.
        self.image_build_id = image_build_id
        # The build task ID.
        self.image_build_job_id = image_build_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_build_id is not None:
            result['ImageBuildId'] = self.image_build_id

        if self.image_build_job_id is not None:
            result['ImageBuildJobId'] = self.image_build_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageBuildId') is not None:
            self.image_build_id = m.get('ImageBuildId')

        if m.get('ImageBuildJobId') is not None:
            self.image_build_job_id = m.get('ImageBuildJobId')

        return self

