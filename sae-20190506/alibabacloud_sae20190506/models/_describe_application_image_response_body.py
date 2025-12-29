# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationImageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationImageResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The information about the image of the application.
        self.data = data
        # The error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The returned message. Valid values:
        # 
        # *   success: If the call is successful, **success** is returned.
        # *   An error code: If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the information about the image was obtained. Valid values:
        # 
        # *   **true**: The information was obtained.
        # *   **false**: The information failed to be obtained.
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeApplicationImageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeApplicationImageResponseBodyData(DaraModel):
    def __init__(
        self,
        cr_url: str = None,
        logo: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_origin_type: str = None,
        repo_tag: str = None,
        repo_type: str = None,
    ):
        # This parameter is reserved.
        self.cr_url = cr_url
        # This parameter is reserved.
        self.logo = logo
        # The region ID.
        self.region_id = region_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The type of the repository. Only Container Registry is supported.
        self.repo_origin_type = repo_origin_type
        # The tag of the image.
        self.repo_tag = repo_tag
        # This parameter is reserved.
        self.repo_type = repo_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cr_url is not None:
            result['CrUrl'] = self.cr_url

        if self.logo is not None:
            result['Logo'] = self.logo

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.repo_origin_type is not None:
            result['RepoOriginType'] = self.repo_origin_type

        if self.repo_tag is not None:
            result['RepoTag'] = self.repo_tag

        if self.repo_type is not None:
            result['RepoType'] = self.repo_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrUrl') is not None:
            self.cr_url = m.get('CrUrl')

        if m.get('Logo') is not None:
            self.logo = m.get('Logo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RepoOriginType') is not None:
            self.repo_origin_type = m.get('RepoOriginType')

        if m.get('RepoTag') is not None:
            self.repo_tag = m.get('RepoTag')

        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')

        return self

