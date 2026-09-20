# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserHdfsInfoRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_id: str = None,
        ext_info: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The cluster ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to obtain the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # dfs.nameservices specifies the nameservices name of DFS. dfs.ha.namenodes specifies the DFS nodes, such as nn1 and nn2.
        # dfs.namenode.http-address.{dfs.nameservices}.nn1 specifies the port 50070 connection of HDFS nn1.
        # dfs.namenode.http-address.{dfs.nameservices}.nn2 specifies the port 50070 connection of HDFS nn2.
        # dfs.namenode.rpc-address.{dfs.nameservices}.nn1 specifies the port 8020 connection of HDFS nn1.
        # dfs.namenode.rpc-address.{dfs.nameservices}.nn2 specifies the port 8020 connection of HDFS nn2.
        # Port 50070 connections and port 8020 connections exist on each HDFS node. The number of port 50070 and port 8020 connection pairs equals the number of HDFS nodes.
        # 
        # This parameter is required.
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        return self

