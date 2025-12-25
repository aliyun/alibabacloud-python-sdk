# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateSqlFromNLRequest(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        dialect: str = None,
        knowledge: str = None,
        level: str = None,
        model: str = None,
        question: str = None,
        real_login_user_uid: str = None,
        table_names: str = None,
    ):
        # This parameter is required.
        self.db_id = db_id
        self.dialect = dialect
        self.knowledge = knowledge
        self.level = level
        self.model = model
        # This parameter is required.
        self.question = question
        self.real_login_user_uid = real_login_user_uid
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.dialect is not None:
            result['Dialect'] = self.dialect

        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge

        if self.level is not None:
            result['Level'] = self.level

        if self.model is not None:
            result['Model'] = self.model

        if self.question is not None:
            result['Question'] = self.question

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Dialect') is not None:
            self.dialect = m.get('Dialect')

        if m.get('Knowledge') is not None:
            self.knowledge = m.get('Knowledge')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        return self

