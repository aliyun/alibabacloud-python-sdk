# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetWebContainerConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        web_container_config: main_models.GetWebContainerConfigResponseBodyWebContainerConfig = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The Tomcat configurations of the application.
        self.web_container_config = web_container_config

    def validate(self):
        if self.web_container_config:
            self.web_container_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.web_container_config is not None:
            result['WebContainerConfig'] = self.web_container_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WebContainerConfig') is not None:
            temp_model = main_models.GetWebContainerConfigResponseBodyWebContainerConfig()
            self.web_container_config = temp_model.from_map(m.get('WebContainerConfig'))

        return self

class GetWebContainerConfigResponseBodyWebContainerConfig(DaraModel):
    def __init__(
        self,
        context_input_type: str = None,
        context_path: str = None,
        http_port: int = None,
        max_threads: int = None,
        server_xml: str = None,
        uri_encoding: str = None,
        use_advanced_server_xml: bool = None,
        use_body_encoding: bool = None,
        use_default_config: bool = None,
    ):
        # The type of the context path.
        self.context_input_type = context_input_type
        # The context path.
        self.context_path = context_path
        # The HTTP service port.
        self.http_port = http_port
        # The maximum number of threads.
        self.max_threads = max_threads
        # The content of the server.xml file customized by using advanced configurations.
        self.server_xml = server_xml
        # The URI encoding scheme.
        self.uri_encoding = uri_encoding
        # Indicates whether advanced configurations are used to customize the server.xml file.
        self.use_advanced_server_xml = use_advanced_server_xml
        # Indicates whether the encoding scheme specified in the request body is used for uniform resource identifier (URI) query parameters.
        self.use_body_encoding = use_body_encoding
        # Indicates whether the default configurations are used.
        self.use_default_config = use_default_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_input_type is not None:
            result['ContextInputType'] = self.context_input_type

        if self.context_path is not None:
            result['ContextPath'] = self.context_path

        if self.http_port is not None:
            result['HttpPort'] = self.http_port

        if self.max_threads is not None:
            result['MaxThreads'] = self.max_threads

        if self.server_xml is not None:
            result['ServerXml'] = self.server_xml

        if self.uri_encoding is not None:
            result['UriEncoding'] = self.uri_encoding

        if self.use_advanced_server_xml is not None:
            result['UseAdvancedServerXml'] = self.use_advanced_server_xml

        if self.use_body_encoding is not None:
            result['UseBodyEncoding'] = self.use_body_encoding

        if self.use_default_config is not None:
            result['UseDefaultConfig'] = self.use_default_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextInputType') is not None:
            self.context_input_type = m.get('ContextInputType')

        if m.get('ContextPath') is not None:
            self.context_path = m.get('ContextPath')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('MaxThreads') is not None:
            self.max_threads = m.get('MaxThreads')

        if m.get('ServerXml') is not None:
            self.server_xml = m.get('ServerXml')

        if m.get('UriEncoding') is not None:
            self.uri_encoding = m.get('UriEncoding')

        if m.get('UseAdvancedServerXml') is not None:
            self.use_advanced_server_xml = m.get('UseAdvancedServerXml')

        if m.get('UseBodyEncoding') is not None:
            self.use_body_encoding = m.get('UseBodyEncoding')

        if m.get('UseDefaultConfig') is not None:
            self.use_default_config = m.get('UseDefaultConfig')

        return self

