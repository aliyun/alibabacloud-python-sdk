# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetContainerConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        container_configuration: main_models.GetContainerConfigurationResponseBodyContainerConfiguration = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The Tomcat configuration.
        self.container_configuration = container_configuration
        # The message returned for the request.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.container_configuration:
            self.container_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.container_configuration is not None:
            result['ContainerConfiguration'] = self.container_configuration.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ContainerConfiguration') is not None:
            temp_model = main_models.GetContainerConfigurationResponseBodyContainerConfiguration()
            self.container_configuration = temp_model.from_map(m.get('ContainerConfiguration'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetContainerConfigurationResponseBodyContainerConfiguration(DaraModel):
    def __init__(
        self,
        context_path: str = None,
        http_port: int = None,
        max_threads: int = None,
        uriencoding: str = None,
        use_body_encoding: bool = None,
    ):
        # The context path of the Tomcat container.
        self.context_path = context_path
        # The application port number for the Tomcat container. The value specified in the application configuration is returned.
        self.http_port = http_port
        # The maximum number of threads in the Tomcat container.
        # 
        # - If no instance group is specified, the configuration of the application is returned.
        # 
        # - If no application is specified, the default configuration is returned.
        self.max_threads = max_threads
        # The Uniform Resource Identifier (URI) encoding scheme. Valid values: ISO-8859-1, GBK, GB2312, and UTF-8.
        # 
        # - If no instance group is specified, the configuration of the application is returned.
        # 
        # - If no application is specified, the default configuration is returned.
        self.uriencoding = uriencoding
        # Indicates whether useBodyEncodingForURI is enabled in the Tomcat container.
        # 
        # - If no instance group is specified, the configuration of the application is returned.
        # 
        # - If no application is specified, the default configuration is returned.
        self.use_body_encoding = use_body_encoding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_path is not None:
            result['ContextPath'] = self.context_path

        if self.http_port is not None:
            result['HttpPort'] = self.http_port

        if self.max_threads is not None:
            result['MaxThreads'] = self.max_threads

        if self.uriencoding is not None:
            result['URIEncoding'] = self.uriencoding

        if self.use_body_encoding is not None:
            result['UseBodyEncoding'] = self.use_body_encoding

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextPath') is not None:
            self.context_path = m.get('ContextPath')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('MaxThreads') is not None:
            self.max_threads = m.get('MaxThreads')

        if m.get('URIEncoding') is not None:
            self.uriencoding = m.get('URIEncoding')

        if m.get('UseBodyEncoding') is not None:
            self.use_body_encoding = m.get('UseBodyEncoding')

        return self

