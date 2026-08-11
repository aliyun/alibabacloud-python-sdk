# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class ListModelPermissionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        list: List[main_models.ListModelPermissionsResponseBodyList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code. This value is empty when the call is successful.
        self.code = code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of workspace permissions.
        self.list = list
        # The maximum number of entries returned per request.
        self.max_results = max_results
        # The token for the next request.
        self.next_token = next_token
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the API call is successful.
        self.success = success
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListModelPermissionsResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListModelPermissionsResponseBodyList(DaraModel):
    def __init__(
        self,
        model: str = None,
        name: str = None,
        permissions: main_models.ListModelPermissionsResponseBodyListPermissions = None,
    ):
        # The model.
        self.model = model
        # The model name.
        self.name = name
        # The authorization status.
        self.permissions = permissions

    def validate(self):
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        if self.permissions is not None:
            result['permissions'] = self.permissions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('permissions') is not None:
            temp_model = main_models.ListModelPermissionsResponseBodyListPermissions()
            self.permissions = temp_model.from_map(m.get('permissions'))

        return self

class ListModelPermissionsResponseBodyListPermissions(DaraModel):
    def __init__(
        self,
        deploy: bool = None,
        fine_tune: bool = None,
        inference: bool = None,
    ):
        # The model deployment authorization. A value of true indicates that the model has been granted authorization. A value of false indicates that the model has not been granted authorization.
        self.deploy = deploy
        # The model training authorization. A value of true indicates that the model has been granted training authorization. A value of false indicates that the model has not been granted authorization.
        self.fine_tune = fine_tune
        # Indicates whether the model has inference permission. A value of true indicates that the model is authorized. A value of false indicates that the model is not authorized.
        self.inference = inference

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy is not None:
            result['deploy'] = self.deploy

        if self.fine_tune is not None:
            result['fineTune'] = self.fine_tune

        if self.inference is not None:
            result['inference'] = self.inference

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploy') is not None:
            self.deploy = m.get('deploy')

        if m.get('fineTune') is not None:
            self.fine_tune = m.get('fineTune')

        if m.get('inference') is not None:
            self.inference = m.get('inference')

        return self

