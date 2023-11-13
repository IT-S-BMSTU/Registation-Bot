// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.19.6
// source: proto/web_api.proto

package pb

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// DataSenderClient is the client API for DataSender service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DataSenderClient interface {
	Create_Bot(ctx context.Context, in *CreateBotRequest, opts ...grpc.CallOption) (*CreateBotResponse, error)
}

type dataSenderClient struct {
	cc grpc.ClientConnInterface
}

func NewDataSenderClient(cc grpc.ClientConnInterface) DataSenderClient {
	return &dataSenderClient{cc}
}

func (c *dataSenderClient) Create_Bot(ctx context.Context, in *CreateBotRequest, opts ...grpc.CallOption) (*CreateBotResponse, error) {
	out := new(CreateBotResponse)
	err := c.cc.Invoke(ctx, "/DataSender/Create_Bot", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DataSenderServer is the server API for DataSender service.
// All implementations should embed UnimplementedDataSenderServer
// for forward compatibility
type DataSenderServer interface {
	Create_Bot(context.Context, *CreateBotRequest) (*CreateBotResponse, error)
}

// UnimplementedDataSenderServer should be embedded to have forward compatible implementations.
type UnimplementedDataSenderServer struct {
}

func (UnimplementedDataSenderServer) Create_Bot(context.Context, *CreateBotRequest) (*CreateBotResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create_Bot not implemented")
}

// UnsafeDataSenderServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DataSenderServer will
// result in compilation errors.
type UnsafeDataSenderServer interface {
	mustEmbedUnimplementedDataSenderServer()
}

func RegisterDataSenderServer(s grpc.ServiceRegistrar, srv DataSenderServer) {
	s.RegisterService(&DataSender_ServiceDesc, srv)
}

func _DataSender_Create_Bot_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateBotRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataSenderServer).Create_Bot(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/DataSender/Create_Bot",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataSenderServer).Create_Bot(ctx, req.(*CreateBotRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// DataSender_ServiceDesc is the grpc.ServiceDesc for DataSender service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var DataSender_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "DataSender",
	HandlerType: (*DataSenderServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Create_Bot",
			Handler:    _DataSender_Create_Bot_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "proto/web_api.proto",
}
