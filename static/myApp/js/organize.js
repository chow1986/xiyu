/**
 * Created by Administrator on 2016/8/4.
 */
var setting = {
    view: {
        dblClickExpand: false
    },
    check: {
        enable: true
    },
    callback: {
        onRightClick: OnRightClick,
        onClick : zTreeOnClick


    }
};
var zNodes =[
    {	rid:101	,	id:	10	,pId:101,name:"	所有机构—",open:true,icon:"../image/1_close.png",nocheck:false,
        children:[
            {id:101, name:"上级机构—", open:true, noR:true,
                children:[
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"}

                ]},
            {id:20, name:"上级部门二", open:true,
                children:[
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"}
                ]},
            {id:30, name:"上级部门三", open:true,
                children:[
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"}
                ]},
            {id:31, name:"上级部门四", open:true,
                children:[
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"}
                ]},
            {id:32, name:"上级部门五", open:true,
                children:[
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"}
                ]},
            {id:33, name:"上级部门六", open:true,
                children:[
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:101, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"},
                    {id:102, name:"中级部门一	", noR:false,icon:"../css/zTreeStyle/img/diy/2.png"}
                ]}
        ]
    }
];
function OnRightClick(event, treeId, treeNode) {
    if (!treeNode && event.target.tagName.toLowerCase() != "button" && $(event.target).parents("a").length == 0) {
        zTree.cancelSelectedNode();
        showRMenu("root", event.clientX, event.clientY);
    } else if (treeNode && !treeNode.noR) {
        zTree.selectNode(treeNode);
        showRMenu("node", event.clientX, event.clientY);
    }
}
function showRMenu(type, x, y) {
    $("#rMenu ul").show();
    if (type=="root") {
        $("#m_del").hide();
        $("#m_check").hide();
        $("#m_unCheck").hide();
    } else {
        $("#m_del").show();
        $("#m_check").show();
        $("#m_unCheck").show();
    }
    rMenu.css({"top":y+"px", "left":x+"px", "visibility":"visible"});

    $("body").bind("mousedown", onBodyMouseDown);
}
function hideRMenu() {
    if (rMenu) rMenu.css({"visibility": "hidden"});
    $("body").unbind("mousedown", onBodyMouseDown);
}
function onBodyMouseDown(event){
    if (!(event.target.id == "rMenu" || $(event.target).parents("#rMenu").length>0)) {
        rMenu.css({"visibility" : "hidden"});
    }
}
var addCount = 1;

//添加事件
        function addTreeNode() {
            $(".div_img").show();
            hideRMenu();
            var newNode = { name:"增加" + (addCount++)};
            if (zTree.getSelectedNodes()[0]) {
                newNode.checked = zTree.getSelectedNodes()[0].checked;
                zTree.addNodes(zTree.getSelectedNodes()[0], newNode);
            } else {
                zTree.addNodes(null, newNode);
            }
        }
//屏蔽右键菜单
function zTreeOnClick(event, treeId, treeNode) {
    treeNodeArrs = treeNode;
    var lists = $('#' + treeId + " li");
    $.each(lists,function(i,item) {
        $('a',item).hasClass("curSelectedNode") && $('a',item).removeClass('curSelectedNode');
    });
    var treeName = $(event.target).html();
    var curElem = $('#' + treeNode.tId);
    !$('a',curElem).first().hasClass("curSelectedNode") && $('a',curElem).first().addClass("curSelectedNode");
    //var pId = treeNode.pId;
    var pId = treeNode.pId;
    if(pId == null) {
        pId = '';
    }

    if(newNode.id == undefined) {
        // 页面一渲染后 页面一有的数据点击 执行下面操作
        getDir(treeNode.id,pId,zTreeArrs[2],'update');
    }else if(newNode.id != undefined && treeNode.name != '') {
        getDir(treeNode.id,pId,zTreeArrs[2],'update');
    }else {
        var index = currentIndex(treeName,zTreeObj);
        if(index > -1 && zTreeObj.length > 1) {
            var idCipherText = zTreeObj[index].idCipherText,
                parentIdCipherText = zTreeObj[index].parentIdCipherText;
            // 新建一项后 再新建第二项 接着点击第二项时候 执行下面操作
            getDir(idCipherText,parentIdCipherText,zTreeArrs[2],'update');
        }else {

            // 当新建一项时候 执行下面的操作
            getDir(newNode.id,newNode.pId,zTreeArrs[2],'update');
        }

    }

    zTreeArrs = [];

};
        function removeTreeNode() {
            hideRMenu();
            var nodes = zTree.getSelectedNodes();
            if (nodes && nodes.length>0) {
                if (nodes[0].children && nodes[0].children.length > 0) {
                    var msg = "要删除的节点是父节点，如果删除将连同子节点一起删掉。\n\n请确认！";
                    if (confirm(msg)==true){
                        zTree.removeNode(nodes[0]);
                    }
                } else {
                    zTree.removeNode(nodes[0]);
                }
            }
        }
        function checkTreeNode(checked) {
            var nodes = zTree.getSelectedNodes();
            if (nodes && nodes.length>0) {
                zTree.checkNode(nodes[0], checked, true);
            }
            hideRMenu();
        }
        function resetTree() {
            hideRMenu();
            $.fn.zTree.init($("#treeDemo"), setting, zNodes);
        }
var zTree, rMenu;
$(document).ready(function(){
    $.fn.zTree.init($("#treeDemo"), setting, zNodes);
    zTree = $.fn.zTree.getZTreeObj("treeDemo");
    rMenu = $("#rMenu");
});