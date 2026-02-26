# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GenerateWebofficeTokenRequest(DaraModel):
    def __init__(
        self,
        cache_preview: bool = None,
        credential_config: main_models.CredentialConfig = None,
        external_uploaded: bool = None,
        filename: str = None,
        hidecmb: bool = None,
        notification: main_models.Notification = None,
        notify_topic_name: str = None,
        password: str = None,
        permission: main_models.WebofficePermission = None,
        preview_pages: int = None,
        project_name: str = None,
        referer: str = None,
        source_uri: str = None,
        user: main_models.WebofficeUser = None,
        user_data: str = None,
        watermark: main_models.WebofficeWatermark = None,
    ):
        # Cache preview flag: 
        # - true: When enabled, the document preview will no longer update collaborative editing content, suitable for scenarios where only preview is needed. 
        # - false: When disabled, it defaults to collaborative preview, allowing the preview to synchronously update collaborative editing content.
        # >Notice: The price for cache preview and non-cache preview differs. Please refer to the billing item description for more details.</notice> >Notice: Search and print functions are not supported during cache preview.</notice> <notice>Updating cached content is currently not supported in cache preview mode.</notice>
        self.cache_preview = cache_preview
        # **If there are no special requirements, leave this blank.**
        # 
        # Chained authorization configuration, not required. For more information, see [Using Chained Authorization to Access Other Entity Resources](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # Indicates whether uploading a file with the same name to OSS is an expected behavior. Possible values are as follows:
        # 
        # - true: Uploading a file with the same name to OSS is an expected behavior. The uploaded document will overwrite the original document and generate a new version. After setting it to true, you still need to close the currently editing document and wait for about 5 minutes before reopening it to load the new document. The upload is only effective when the document is closed; if the document is open, the new save will overwrite the uploaded file.
        # - false (default): Uploading a file with the same name to OSS is not an expected behavior, and the interface will return an error.
        self.external_uploaded = external_uploaded
        # Filename, which must include the file extension. By default, it is the last segment of the **SourceURI** parameter.
        # Supported file extensions (PDF is only supported for preview):
        # - Text documents (Word): doc, docx, txt, dot, wps, wpt, dotx, docm, dotm, rtf 
        # - Presentation documents (PPT): ppt, pptx, pptm, ppsx, ppsm, pps, potx, potm, dpt, dps - Spreadsheet documents (Excel): et, xls, xlt, xlsx, xlsm, xltx, xltm, csv 
        # - PDF documents: pdf
        self.filename = filename
        # Whether to hide the toolbar. This parameter can be set in document preview mode. Possible values are as follows:
        # 
        # - false (default): Do not hide the toolbar.
        # - true: Hide the toolbar.
        self.hidecmb = hidecmb
        # Notification message configuration, currently supporting only MNS. For the asynchronous notification message format, refer to [WebOffice Message Notification Format](https://help.aliyun.com/document_detail/2743999.html).
        # 
        # > There will be message notifications when the file is saved or renamed.
        self.notification = notification
        # Supports notifying some events to customers via MNS messages. This parameter is the topic for MNS asynchronous message notifications.
        self.notify_topic_name = notify_topic_name
        # The password to open the document.
        # > If you need to preview or edit a password-protected document, set this parameter.
        self.password = password
        # User permission information, represented in JSON format.
        # 
        # User permissions include the following options:
        # 
        # Each option is of type Boolean, with a default value of false, and can be set to true or false.
        # 
        # - Readonly (optional): Preview mode.
        # - Rename (optional): File renaming permission, which only provides message notification functionality. The renaming event will be sent to MNS.
        # - History (optional): Permission to view historical versions.
        # - Copy (optional): Copy permission.
        # - Export (optional): PDF export permission.
        # - Print (optional): Print permission.
        # 
        # >PDF only supports preview functionality, so the "Readonly" parameter must be set to true.
        # >
        # >PDF files do not support exporting.
        # > 
        # >To use the multi-version feature, you must first enable the multi-version feature in OSS and then set the "History" parameter to true.
        # >
        # >Notice: Printing is not supported in cached preview.
        # >Notice: Historical versions can be viewed in edit mode but not in preview mode.
        self.permission = permission
        # Limits the number of pages that can be previewed. By default, there is no limit. The maximum cannot exceed 5000.
        self.preview_pages = preview_pages
        # Project name, for how to obtain it, please refer to [Create Project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # OSS anti-leeching. IMM needs to obtain the source file from OSS. If OSS has set up anti-leeching, IMM must pass the corresponding header to OSS to get the source file.
        # > If the Bucket where the document is located has Referer set, please configure this parameter.
        self.referer = referer
        # OSS address of the document to be previewed or edited. The OSS address follows the rule `oss://${Bucket}/${Object}`, where `Bucket` is the name of the OSS Bucket in the same region as the current project, and `Object` is the full path of the file including the file extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # User information. You can pass in user information from the business side, which will be displayed on the WebOffice page.
        # 
        # The system distinguishes different users by User.Id, and User.Name is used only for front-end display. If User.Id is not provided, the backend will generate a random ID. Users with different IDs are considered different entities and cannot modify or delete each other\\"s comments.
        # 
        # The default format is: Unknown_random string. If User.Id is not provided, the user information will default to "Unknown".
        self.user = user
        # User-defined information. It only takes effect when Notification parameters are filled in for MNS configuration. It will be returned in asynchronous message notifications, which can help you correlate and process messages within your system. The maximum length is 2048 bytes.
        self.user_data = user_data
        # Watermark information. The watermark is generated on the front end and is not written into the source document. The same document with different parameters will result in different watermarks.
        self.watermark = watermark

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.permission:
            self.permission.validate()
        if self.user:
            self.user.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_preview is not None:
            result['CachePreview'] = self.cache_preview

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.external_uploaded is not None:
            result['ExternalUploaded'] = self.external_uploaded

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name

        if self.password is not None:
            result['Password'] = self.password

        if self.permission is not None:
            result['Permission'] = self.permission.to_map()

        if self.preview_pages is not None:
            result['PreviewPages'] = self.preview_pages

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.referer is not None:
            result['Referer'] = self.referer

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.user is not None:
            result['User'] = self.user.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachePreview') is not None:
            self.cache_preview = m.get('CachePreview')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('ExternalUploaded') is not None:
            self.external_uploaded = m.get('ExternalUploaded')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Permission') is not None:
            temp_model = main_models.WebofficePermission()
            self.permission = temp_model.from_map(m.get('Permission'))

        if m.get('PreviewPages') is not None:
            self.preview_pages = m.get('PreviewPages')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('User') is not None:
            temp_model = main_models.WebofficeUser()
            self.user = temp_model.from_map(m.get('User'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('Watermark') is not None:
            temp_model = main_models.WebofficeWatermark()
            self.watermark = temp_model.from_map(m.get('Watermark'))

        return self

