# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListSecretValueResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        secrets: List[main_models.ListSecretValueResponseBodySecrets] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The list of secrets.
        self.secrets = secrets

    def validate(self):
        if self.secrets:
            for v1 in self.secrets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['secrets'] = []
        if self.secrets is not None:
            for k1 in self.secrets:
                result['secrets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.secrets = []
        if m.get('secrets') is not None:
            for k1 in m.get('secrets'):
                temp_model = main_models.ListSecretValueResponseBodySecrets()
                self.secrets.append(temp_model.from_map(k1))

        return self

class ListSecretValueResponseBodySecrets(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content: str = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        name: str = None,
        secret_id: str = None,
        secret_type: str = None,
    ):
        # The comment.
        self.comment = comment
        # The secret content.
        self.content = content
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The UID of the creator.
        self.creator = creator
        # The nickname of the creator.
        self.creator_name = creator_name
        # The secret name.
        self.name = name
        # The secret ID.
        self.secret_id = secret_id
        # The secret type. The value is fixed to secret.
        self.secret_type = secret_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.content is not None:
            result['content'] = self.content

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.name is not None:
            result['name'] = self.name

        if self.secret_id is not None:
            result['secretId'] = self.secret_id

        if self.secret_type is not None:
            result['secretType'] = self.secret_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('secretId') is not None:
            self.secret_id = m.get('secretId')

        if m.get('secretType') is not None:
            self.secret_type = m.get('secretType')

        return self

