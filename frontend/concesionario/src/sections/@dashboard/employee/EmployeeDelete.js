import React, { useContext } from "react";
import Modal from "@mui/material/Modal";
import { useTranslation } from "react-i18next";
import {
    Box,
    Button,
    Stack,
    Typography,
} from "@mui/material";
import useMediaQuery from "@mui/material/useMediaQuery";
import { useTheme } from "@mui/material/styles";
import EmployeeContext from "../../../hooks/employee/EmployeeContext";

export default function EmployeeDelete() {

    const { employee, openDelete, handleCloseDelete, handleDelete } = useContext(EmployeeContext);

    const theme = useTheme();
    const isSmallScreen = useMediaQuery(theme.breakpoints.down("sm"));

    const modalStyle = {
        position: "absolute",
        top: "50%",
        left: "50%",
        transform: "translate(-50%, -50%)",
        width: isSmallScreen ? "90%" : "70%",
        height: isSmallScreen ? "25%" : "auto",
        overflowY: "auto",
        bgcolor: "background.paper",
        boxShadow: 24,
        p: 4,
        borderRadius: 2,
    };

    const { t, i18n } = useTranslation("lang");

    return (
        <Modal
            open={openDelete}
            onClose={handleCloseDelete}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box sx={modalStyle}>
                <Stack direction="row" alignItems="center" justifyContent="space-between" mb={2}>
                    <Typography variant="h4" gutterBottom>
                        {t('empleados.encabezado.eliminar')}
                    </Typography>
                </Stack>
                <Typography variant="body1" gutterBottom>
                    {t('empleados.mensaje.confirmacionEliminar', {cedula: employee.cedula})}
                </Typography>
                <Stack direction="row" spacing={2} justifyContent="flex-end">
                    <Button variant="contained" onClick={handleCloseDelete}>
                        {t('general.botones.no')}
                    </Button>
                    <Button variant="contained" color="error" onClick={handleDelete}>
                        {t('general.botones.si')}
                    </Button>
                </Stack>
            </Box>
        </Modal>
    );
}