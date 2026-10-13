# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceResponseBody(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        dry_run: bool = None,
        dry_run_result: bool = None,
        message: str = None,
        order_id: str = None,
        port: str = None,
        request_id: str = None,
        tag_result: bool = None,
        task_id: str = None,
    ):
        # The internal endpoint of the instance.
        self.connection_string = connection_string
        # The instance ID. If you set the **Amount** parameter to a value greater than **1**, the response contains the specified number of instance IDs separated by commas.
        # 
        # For example, if you set the **Amount** parameter to **3**, the response contains three instance IDs. Example:
        # `rm-uf6wjk5*****1,rm-uf6wjk5*****2,rm-uf6wjk5*****3`
        self.dbinstance_id = dbinstance_id
        # Indicates whether a dry run was performed before the instance was created.
        # 
        # * The value is fixed to **true**.
        # * If no dry run is performed, this parameter is not returned.
        self.dry_run = dry_run
        # Indicates whether the dry run passed. Valid values:
        # * **true**: The dry run passed.
        # * **false**: The dry run failed.
        # 
        # > * If no dry run is performed, this parameter is not returned.
        # > * If the dry run fails, the corresponding error is returned.
        self.dry_run_result = dry_run_result
        # The prompt message for the batch creation task.
        # 
        # > This parameter is returned only when the **Amount** parameter is set to a value greater than 1.
        self.message = message
        # The order ID.
        self.order_id = order_id
        # The port number of the internal endpoint of the instance.
        self.port = port
        # The request ID.
        self.request_id = request_id
        # Indicates whether the instance was successfully tagged. Valid values:
        # * **true**: The instance was successfully tagged.
        # * **false**: The instance failed to be tagged.
        # 
        # > If no tags are bound to the instance, this parameter is not returned.
        self.tag_result = tag_result
        # The task ID of the batch creation task.
        # 
        # * This parameter is returned only when the **Amount** parameter is set to a value greater than 1.
        # * You cannot query the task by using the **TaskId** value.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result

        if self.message is not None:
            result['Message'] = self.message

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.port is not None:
            result['Port'] = self.port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_result is not None:
            result['TagResult'] = self.tag_result

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('DryRunResult') is not None:
            self.dry_run_result = m.get('DryRunResult')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagResult') is not None:
            self.tag_result = m.get('TagResult')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

