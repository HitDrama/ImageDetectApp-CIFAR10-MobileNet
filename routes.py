from flask import Blueprint

from controllers.lession_tranfer_controller import lession_transfer


deep_router=Blueprint("deep",__name__)

#định nghĩa router

deep_router.route("/lession-transfer",methods=["GET","POST"])(lession_transfer)
