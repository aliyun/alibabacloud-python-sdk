# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class UpdateABTestSceneRequest(DaraModel):
    def __init__(
        self,
        body: main_models.ABTestScene = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.ABTestScene()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

