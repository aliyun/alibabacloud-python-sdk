# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContainerConfigurationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        context_path: str = None,
        group_id: str = None,
        http_port: int = None,
        max_threads: int = None,
        uriencoding: str = None,
        use_body_encoding: bool = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The context path of the Tomcat container. The context path can be an empty string, a null WAR package name, a root directory, or other custom non-empty strings. It can contain letters, digits, hyphens (-), and underscores (_). Take note of the following items:
        # 
        # *   If this parameter is not specified when you configure the application instance group, the configuration of the application is applied.
        # *   If this parameter is not specified when you configure the Tomcat container for an application, the root directory `/` is used.
        self.context_path = context_path
        # The ID of the application instance group.
        # 
        # *   If an ID is specified, this operation configures the Tomcat container for the specified application instance group.
        # *   If you set this parameter to "", this operation configures the Tomcat container for the application.
        self.group_id = group_id
        # The application port number for the Tomcat container. Take note of the following items:
        # 
        # *   If this parameter is not specified when you configure the application instance group, the configuration of the application is applied.
        # *   If this parameter is not specified when you configure the application, the default port 8080 is applied.
        self.http_port = http_port
        # The maximum number of threads. Take note of the following items:
        # 
        # *   If this parameter is not specified when you configure the application instance group, the configuration of the application is applied.
        # *   If this parameter is not specified when you configure the application, the default value 250 is applied.
        self.max_threads = max_threads
        # The uniform resource identifier (URI) encoding scheme. Valid values: ISO-8859-1, GBK, GB2312, and UTF-8. Take note of the following items:
        # 
        # *   If this parameter is not specified when you configure the application instance group, the configuration of the application is applied.
        # *   If this parameter is not specified when you configure the application, the default URI encoding scheme in the Tomcat container is applied.
        self.uriencoding = uriencoding
        # Specifies whether to use the encoding scheme specified in the request body for URI query parameters. Take note of the following items:
        # 
        # *   If this parameter is not specified when you configure the application instance group, the configuration of the application is applied.
        # *   If this parameter is not specified when you configure the application, the default value false is applied.
        self.use_body_encoding = use_body_encoding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.context_path is not None:
            result['ContextPath'] = self.context_path

        if self.group_id is not None:
            result['GroupId'] = self.group_id

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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ContextPath') is not None:
            self.context_path = m.get('ContextPath')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('MaxThreads') is not None:
            self.max_threads = m.get('MaxThreads')

        if m.get('URIEncoding') is not None:
            self.uriencoding = m.get('URIEncoding')

        if m.get('UseBodyEncoding') is not None:
            self.use_body_encoding = m.get('UseBodyEncoding')

        return self

