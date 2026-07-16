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
        # Specifies whether to enable cached preview.
        # 
        # -  true: When enabled, the document preview no longer updates collaborative editing content. This is suitable for preview-only scenarios.
        # -  false: When disabled, collaborative preview is used by default, which synchronizes collaborative editing content during preview.
        # 
        # >Notice: Cached preview and non-cached preview have different unit prices. For more information, see the billing item description.
        # </notice>>Notice: Cached preview does not support document content search or printing.</notice>
        # <notice>Cached preview does not support updating cached content.</notice>.
        self.cache_preview = cache_preview
        # **Leave this parameter empty unless you have specific requirements.**
        # 
        # The China authorization configuration. This parameter is optional. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # Specifies whether uploading a file with the same name to OSS is expected behavior. Valid values:
        # 
        # - true: Uploading a file with the same name to OSS is expected behavior. The uploaded document overwrites the original document and generates a new version. After this parameter is set to true, you must first close the document that is being edited, wait about 5 minutes, and then reopen it to load the new document. The upload takes effect only when the document is closed. If the document is open, new saves overwrite the uploaded file.
        # - false (default): Uploading a file with the same name to OSS is not expected behavior. The operation returns an error.
        self.external_uploaded = external_uploaded
        # The file name, which must include the file name extension. The default value is the last segment of the **SourceURI** parameter.
        # 
        # Supported file name extensions (PDF supports preview only):
        # 
        # - Word documents: doc, docx, txt, dot, wps, wpt, dotx, docm, dotm, and rtf
        # - PowerPoint documents: ppt, pptx, pptm, ppsx, ppsm, pps, potx, potm, dpt, and dps
        # - Excel documents: et, xls, xlt, xlsx, xlsm, xltx, xltm, and csv
        # - PDF documents: pdf.
        self.filename = filename
        # Specifies whether to hide the toolbar. This parameter is supported in document preview mode. Valid values:
        # 
        # - false (default): The toolbar is not hidden.
        # 
        # - true: The toolbar is hidden.
        self.hidecmb = hidecmb
        # The notification configuration. Currently, only MNS is supported. For the format of asynchronous notification messages, see [WebOffice message notification format](https://help.aliyun.com/document_detail/2743999.html).
        # 
        # > Message notifications are sent when a file is saved or renamed.
        self.notification = notification
        # Sends event notifications to you as MNS messages. This parameter specifies the MNS topic for asynchronous message notifications.
        self.notify_topic_name = notify_topic_name
        # The password to open the document.
        # > Set this parameter if you want to preview or edit a password-protected document.
        self.password = password
        # The user permission information in JSON format.
        # 
        # User permissions include the following options:
        # 
        # Each option is of the Boolean type. The default value is false. Valid values: true and false.
        # 
        # - Readonly (optional): Preview mode.
        # 
        # - Rename (optional): The permission to rename a file. Only message notification is provided. The rename event is sent to MNS.
        # 
        # - History (optional): The permission to view historical versions.
        # 
        # - Copy (optional): The copy permission.
        # 
        # - Export (optional): The permission to export to PDF.
        # 
        # - Print (optional): The print permission.
        # 
        # 
        # > PDF supports only the preview feature. You must set the Readonly parameter to true.
        # >
        # 
        # > PDF files do not support export.
        # > 
        # 
        # > To use the versioning feature, you must first enable versioning in OSS and then set the History parameter to true.
        # >
        # >Notice: Printing is not supported in cached preview.
        # >Notice: Historical versions can be viewed in edit mode but not in preview mode..
        self.permission = permission
        # The maximum number of pages that can be previewed. By default, no limit is imposed. The maximum value is 5,000.
        self.preview_pages = preview_pages
        # The project name. For information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The OSS hotlink protection referer. Intelligent Media Management (IMM) needs to retrieve the source file from OSS. If hotlink protection is configured for OSS, IMM must pass the corresponding header to OSS to retrieve the source file.
        # > Set this parameter if the bucket that stores the document has a referer configured.
        self.referer = referer
        # The OSS URI of the document to preview or edit.
        # 
        # The OSS URI follows the format `oss://${Bucket}/${Object}`, where `Bucket` is the name of an OSS bucket in the same region as the current project, and `Object` is the full path of the file including the file name extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The user information. You can pass in user information from the business side, and the WebOffice page displays this information.
        # 
        # The system distinguishes different users by User.Id. User.Name is used only for frontend display. If User.Id is not specified, the backend automatically generates a random ID. Users with different IDs are treated as different principals and cannot modify or delete each other\\"s comments.
        # 
        # The default format is: Unknown_RandomString. If User.Id is not specified, the user information is displayed as "Unknown" by default.
        self.user = user
        # The custom user data. This parameter takes effect only when the Notification parameter is specified with MNS configurations. The data is returned in asynchronous message notifications for you to associate and process message notifications within your system. Maximum length: 2,048 bytes.
        self.user_data = user_data
        # The watermark information. The watermark is generated on the frontend and is not written to the source document. Different parameters passed for the same document produce different watermarks.
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

