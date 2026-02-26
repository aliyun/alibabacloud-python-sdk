# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExtractDocumentTextShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_type: str = None,
        source_uri: str = None,
    ):
        # **If there are no special requirements, leave it blank.**
        # 
        # Chain authorization configuration, optional. For more information, see [Using Chain Authorization to Access Other Entity Resources](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # Project name. For how to obtain it, see [Creating a Project](https://help.aliyun.com/document_detail/477051.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Suffix type of the source data. By default, the type of the source data is determined based on the suffix of the input object. When the input object does not have a suffix, you can set this parameter. The available values are as follows:
        # 
        # - Word Documents: doc, docx, wps, wpss, docm, dotm, dot, dotx, html
        # - Presentation Documents (PPT): pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, dpss
        # - Spreadsheet Documents (Excel): xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, ets
        # - PDF Documents: pdf
        self.source_type = source_type
        # Storage address of the source data.
        # 
        # The OSS address rule is oss://${Bucket}/${Object}, where `${Bucket}` is the name of the OSS Bucket in the same region (Region) as the current project, and `${Object}` is the complete path of the file including the file extension.
        # >Notice: Currently, only HTTP protocol addresses are supported.
        # 
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        return self

