# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class CreateFpShotDBResponseBody(DaraModel):
    def __init__(
        self,
        fp_shot_db: main_models.CreateFpShotDBResponseBodyFpShotDB = None,
        request_id: str = None,
    ):
        # The details of the media fingerprint library.
        self.fp_shot_db = fp_shot_db
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fp_shot_db:
            self.fp_shot_db.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_shot_db is not None:
            result['FpShotDB'] = self.fp_shot_db.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpShotDB') is not None:
            temp_model = main_models.CreateFpShotDBResponseBodyFpShotDB()
            self.fp_shot_db = temp_model.from_map(m.get('FpShotDB'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateFpShotDBResponseBodyFpShotDB(DaraModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        fp_dbid: str = None,
        model_id: int = None,
        name: str = None,
        state: str = None,
    ):
        # The configurations of the media fingerprint library.
        self.config = config
        # The description of the media fingerprint library.
        self.description = description
        # The ID of the media fingerprint library. We recommend that you keep this ID for subsequent operation calls.
        self.fp_dbid = fp_dbid
        # The model ID of the media fingerprint library.
        self.model_id = model_id
        # The name of the media fingerprint library.
        self.name = name
        # The status of the media fingerprint library. After the media fingerprint library is created, it enters the **offline** state. After the media fingerprint library is processed at the backend, it enters the **active** state.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

