# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListFpShotDBResponseBody(DaraModel):
    def __init__(
        self,
        fp_shot_dblist: main_models.ListFpShotDBResponseBodyFpShotDBList = None,
        non_exist_ids: main_models.ListFpShotDBResponseBodyNonExistIds = None,
        request_id: str = None,
    ):
        self.fp_shot_dblist = fp_shot_dblist
        self.non_exist_ids = non_exist_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fp_shot_dblist:
            self.fp_shot_dblist.validate()
        if self.non_exist_ids:
            self.non_exist_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_shot_dblist is not None:
            result['FpShotDBList'] = self.fp_shot_dblist.to_map()

        if self.non_exist_ids is not None:
            result['NonExistIds'] = self.non_exist_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpShotDBList') is not None:
            temp_model = main_models.ListFpShotDBResponseBodyFpShotDBList()
            self.fp_shot_dblist = temp_model.from_map(m.get('FpShotDBList'))

        if m.get('NonExistIds') is not None:
            temp_model = main_models.ListFpShotDBResponseBodyNonExistIds()
            self.non_exist_ids = temp_model.from_map(m.get('NonExistIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFpShotDBResponseBodyNonExistIds(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

class ListFpShotDBResponseBodyFpShotDBList(DaraModel):
    def __init__(
        self,
        fp_shot_db: List[main_models.ListFpShotDBResponseBodyFpShotDBListFpShotDB] = None,
    ):
        self.fp_shot_db = fp_shot_db

    def validate(self):
        if self.fp_shot_db:
            for v1 in self.fp_shot_db:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShotDB'] = []
        if self.fp_shot_db is not None:
            for k1 in self.fp_shot_db:
                result['FpShotDB'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot_db = []
        if m.get('FpShotDB') is not None:
            for k1 in m.get('FpShotDB'):
                temp_model = main_models.ListFpShotDBResponseBodyFpShotDBListFpShotDB()
                self.fp_shot_db.append(temp_model.from_map(k1))

        return self

class ListFpShotDBResponseBodyFpShotDBListFpShotDB(DaraModel):
    def __init__(
        self,
        description: str = None,
        fp_dbid: str = None,
        model_id: int = None,
        name: str = None,
        status: str = None,
    ):
        self.description = description
        self.fp_dbid = fp_dbid
        self.model_id = model_id
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

